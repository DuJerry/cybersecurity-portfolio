# Network Reconnaissance and Port Scanning Analysis

## 1. Objective
The objective of this project was to perform authorized network reconnaissance and service enumeration against a controlled local lab environment. By combining Nmap scanning techniques with custom Python port-scanning scripts, the project identifies exposed TCP/UDP services, analyzes potential attack surfaces, and defines host-hardening remediations.

## 2. Environment and Tools
* **Scanner Environment:** macOS / Kali Linux Local Lab Host
* **Target Environment:** Authorized Local Course Lab Target (`127.0.0.1` / Private Lab Subnet)
* **Tools & Scripts:** Nmap, Python 3 (`socket` / `python-nmap` — see [`requirements.txt`](./evidence/requirements.txt))

## 3. Step-by-Step Method
1. **Host & Port Discovery:** Executed TCP SYN and connect scans (`nmap -sS -sV`) against the authorized local lab target to enumerate active ports and service banners.
2. **Automated Script Verification:** Ran custom Python scanning script ([`port-scanner.py`](./evidence/port-scanner.py)) to cross-verify open ports and response timeouts.
3. **Service & Risk Analysis:** Evaluated each discovered port and service version against common security misconfigurations (such as unencrypted protocols or unnecessary exposed daemons).

## 4. Results and Evidence
The scan successfully mapped active services on the local target and highlighted exposed ports requiring access restrictions.

* **Custom Scanner Script & Dependencies:** [`port-scanner.py`](./evidence/port-scanner.py) | [`requirements.txt`](./evidence/requirements.txt)
* **Scan Output Proof:** ![Scan Output](./evidence/nmap-scan-output.png)

*(Note: Ensure the filenames above match the actual files placed inside your `evidence/` folder.)*

## 5. Remediation and Hardening Recommendations
* **Minimize Attack Surface:** Disable unused network services and close unnecessary listening ports on the host.
* **Enforce Encryption:** Replace any cleartext services (such as HTTP, Telnet, or FTP) with encrypted equivalents (HTTPS, SSH, SFTP).
* **Firewall Filtering:** Apply host-based firewall rules to restrict service access strictly to authorized administrative IP addresses.
