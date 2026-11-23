# ARP Spoofing and Traffic Interception Lab in Kathara

## 1. Objective
The objective of this lab was to simulate an Address Resolution Protocol (ARP) cache poisoning (Man-in-the-Middle) attack inside an isolated Kathara virtual network environment. By crafting spoofed ARP replies using Python and Scapy, the project demonstrates how the lack of authentication in Layer-2 ARP allows an attacker on the same broadcast domain to intercept unencrypted HTTP traffic between two victim hosts, and highlights necessary Layer-2 defenses.

## 2. Environment and Tools
* **Network Emulation Platform:** Kathara (Container-based virtual network lab)
* **Topology Nodes:** Two victim hosts (`h1`, `h2`) and one attacker node (`attacker`) on a shared Layer-2 collision domain configured via `lab.conf`
* **Tools & Scripts:** Python 3, Scapy (`scapy-arp-spoof.py`, `httpd-sniff.py`), `arp`, `iproute2`, `tcpdump`

## 3. Step-by-Step Method
1. **Lab Environment Setup:** Defined the virtual network topology in `lab.conf` and initialized IP addressing and routing parameters via node startup scripts (`h1.startup`, `h2.startup`, `attacker.startup`).
2. **Baseline Verification:** Verified normal Layer-2 MAC-to-IP mappings on `h1` and `h2` using `arp -a` prior to launching the attack.
3. **IP Forwarding & ARP Poisoning:** Enabled IP forwarding on the `attacker` container so intercepted packets would still reach their intended destination without causing a Denial of Service, then executed `scapy-arp-spoof.py` to send forged ARP replies associating the attacker's MAC address with both victims' IP addresses.
4. **Traffic Sniffing:** Ran `httpd-sniff.py` on the attacker node to capture and inspect unencrypted HTTP requests passing through the poisoned path.

## 4. Results and Evidence
The ARP tables on both `h1` and `h2` were successfully updated to map each other's IP addresses to the `attacker` node's MAC address, enabling transparent interception of cleartext HTTP traffic.

* **Lab Topology & Startup Scripts:** [`lab.conf`](./evidence/lab.conf) | [`attacker.startup`](./evidence/attacker.startup) | [`h1.startup`](./evidence/h1.startup) | [`h2.startup`](./evidence/h2.startup)
* **Custom Scapy Scripts:** [`scapy-arp-spoof.py`](./evidence/scapy-arp-spoof.py) | [`httpd-sniff.py`](./evidence/httpd-sniff.py)
* **Attack & Packet Capture Proof:** ![ARP Spoofing Proof](./evidence/arp-spoof-result.png)

## 5. Remediation and Defensive Countermeasures
* **Dynamic ARP Inspection (DAI):** Configure enterprise switches to validate ARP packets against a trusted DHCP snooping binding database and drop forged ARP replies.
* **Static ARP Entries:** For critical infrastructure hosts (such as default gateways), configure static MAC-to-IP bindings where operationally feasible.
* **End-to-End Encryption (HTTPS/TLS):** Enforce HTTPS with HSTS so that even if Layer-2 traffic is intercepted via ARP spoofing, credentials and session payloads remain encrypted and tamper-evident.
