#!/usr/bin/env python3
import argparse
import datetime
import json
import os
import sys
import time
from typing import Dict, Any, List
from scapy.all import IP, TCP, ICMP, sr1, send, PcapWriter

class SynScanner:
    def __init__(self, scope_path: str, output_path: str, dry_run: bool = False, execute: bool = False):
        self.scope_path = scope_path
        self.output_path = output_path
        self.dry_run = dry_run
        self.execute = execute
        self.scope = self._load_and_validate_scope()
   #[参数/Scope 解析] ➔ [输入安全校验] ➔ [Dry-Run/发包决策] ➔ [Scapy 探测与匹配] ➔ [结果分类/输出 JSON]
    def _load_and_validate_scope(self) -> Dict[str, Any]:
        if not os.path.exists(self.scope_path):
            print(f"Error: Scope file {self.scope_path} not found.", file=sys.stderr)
            sys.exit(1)
            
        with open(self.scope_path, "r", encoding="utf-8") as f:
            try:
                scope = json.load(f)
            except json.JSONDecodeError:
                print("Error: Invalid JSON in scope file.", file=sys.stderr)
                sys.exit(1)

        required_fields = ["scope_id", "option", "target", "ports", "maximum_rate_pps", "maximum_attempts", "timeout_seconds"]
        for field in required_fields:
            if field not in scope:
                print(f"Error: Missing required field '{field}' in scope JSON.", file=sys.stderr)
                sys.exit(1)

        if scope["option"] != "tcp-syn-scan":
            print(f"Error: Unsupported option '{scope['option']}'. Expected 'tcp-syn-scan'.", file=sys.stderr)
            sys.exit(1)

        if len(scope["ports"]) > 30:
            print("Error: Scope exceeds maximum limit of 30 ports.", file=sys.stderr)
            sys.exit(1)
            
        return scope

    def run(self) -> Dict[str, Any]:
        if not self.execute and not self.dry_run:
            print("Error: Must specify either --dry-run or --execute.", file=sys.stderr)
            sys.exit(1)

        target = self.scope["target"]
        ports = self.scope["ports"]
        timeout = self.scope.get("timeout_seconds", 1.5)
        max_rate = self.scope.get("maximum_rate_pps", 20)
        delay = 1.0 / max_rate
        
        start_time = datetime.datetime.now(datetime.timezone.utc).isoformat()
        results = []
        captured_packets = []

        print(f"[*] Starting TCP SYN Scan against {target} (Scope ID: {self.scope['scope_id']})")
        
        if self.dry_run:
            print("[*] DRY RUN MODE: No network traffic will be generated.")
            for p in ports:
                results.append({"port": p, "status": "dry-run-planned"})
        else:
            for port in ports:
                status = "filtered-or-no-response"
                attempts = self.scope.get("maximum_attempts", 2)
                
                for attempt in range(attempts):
                    syn_packet = IP(dst=target)/TCP(dport=port, flags="S")
                    captured_packets.append(syn_packet)
                    
                    resp = sr1(syn_packet, timeout=timeout, verbose=0)
                    time.sleep(delay)
                    
                    if resp:
                        captured_packets.append(resp)
                        if resp.haslayer(TCP):
                            flags = resp.getlayer(TCP).flags
                            if flags & 0x12 == 0x12:
                                status = "open"
                                rst_packet = IP(dst=target)/TCP(dport=port, flags="R")
                                send(rst_packet, verbose=0)
                                captured_packets.append(rst_packet)
                                break
                            elif flags & 0x04:
                                status = "closed"
                                break
                        elif resp.haslayer(ICMP):
                            icmp_type = resp.getlayer(ICMP).type
                            icmp_code = resp.getlayer(ICMP).code
                            if icmp_type == 3 and icmp_code in [1, 2, 3, 9, 10, 13]:
                                status = "filtered-or-no-response"
                                break
                
                results.append({"port": port, "status": status})

        end_time = datetime.datetime.now(datetime.timezone.utc).isoformat()
        
        if not self.dry_run and captured_packets:
            pcap_path = os.path.join(os.path.dirname(self.output_path), "experiment.pcap")
            writer = PcapWriter(pcap_path, append=False, sync=True)
            for pkt in captured_packets:
                writer.write(pkt)

        output_data = {
            "scope_id": self.scope["scope_id"],
            "tool_version": "1.0.0",
            "option": self.scope["option"],
            "utc_window": {"start": start_time, "end": end_time},
            "target": target,
            "scan_results": results
        }

        with open(self.output_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2)

        print(f"[+] Scan finished. Output saved to {self.output_path}")
        return output_data

def main():
    parser = argparse.ArgumentParser(description="Scapy TCP SYN Scanner")
    parser.add_argument("--scope", required=True, help="Path to scope.json")
    parser.add_argument("--output", required=True, help="Path to output result.json")
    parser.add_argument("--dry-run", action="store_true", help="Perform dry run without sending packets")
    parser.add_argument("--execute", action="store_true", help="Execute real scan")
    
    args = parser.parse_args()
    scanner = SynScanner(args.scope, args.output, dry_run=args.dry_run, execute=args.execute)
    scanner.run()

if __name__ == "__main__":
    main()