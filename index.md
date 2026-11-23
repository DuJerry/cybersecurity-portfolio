---
layout: home
title: Home
---

# Jerry Du — Cybersecurity Portfolio

## 1. About Me

I am a Master of Cyber Security candidate at Universiti Malaya (UM), building upon a Bachelor of Engineering in Computer Science and Technology from Henan University. With a solid academic foundation in software development, algorithms, and computer networks, my primary focus lies at the intersection of software engineering and defensive security.

My interest in cybersecurity grew from recognizing that many critical vulnerabilities stem from insecure design and implementation flaws at the code and protocol levels. Rather than treating security as an afterthought, I am passionate about building resilient software systems and understanding adversarial mechanics—from Layer-2 network manipulation to automated reconnaissance—so I can engineer stronger defenses. Through my postgraduate coursework and hands-on lab projects, I am actively bridging my programming background with practical network and application security skills.

---

## 2. Technical Skills

* **Python Security Scripting & Automation (Confident):** Demonstrated in [ARP Spoofing and Traffic Interception Lab](./projects/kathara-arp-spoofing/) and [Network Reconnaissance and Port Scanning Analysis](./projects/nmap-service-scan/)
* **Network Reconnaissance & Service Enumeration (Working Knowledge):** Demonstrated in [Network Reconnaissance and Port Scanning Analysis](./projects/nmap-service-scan/)
* **Virtual Network Emulation & Protocol Analysis (Working Knowledge):** Demonstrated in [ARP Spoofing and Traffic Interception Lab](./projects/kathara-arp-spoofing/)
* **Linux Command Line & Containerized Labs (Working Knowledge):** Applied across Kathara and local security testing environments
* **Secure Software Engineering & Web Security (Beginner):** Currently expanding through postgraduate security programming and penetration defense coursework

---

## 3. Certifications and Training

* **Software Design Engineer Qualification (软考软件设计师 / Software Engineer)** — Certified by the Ministry of Industry and Information Technology (MIIT), China (Earned)
* **Master of Cyber Security Program (2026/2027 Cohort)** — Universiti Malaya (In Progress, Expected Graduation: 2027)
  * *Semester I (2026/2027):* WQE7001 Cyber Security, WQE7002 Advanced Network Security Programming, WQE7007 Network Technology and Security
  * *Upcoming Core & Elective Focus (2027):* WQE7003 Cryptography and Information Hiding, WQE7004 Information Assurance, WQE7005 Advanced Digital Forensics, WQE7011 Advanced Computer Penetration and Defense
* **ISC2 Certified in Cybersecurity (CC)** — Self-paced Study Path (In Progress, Target: March 2027)

---

## 4. Projects

1. **[ARP Spoofing and Traffic Interception Lab in Kathara](./projects/kathara-arp-spoofing/)**
   Simulated a Layer-2 Man-in-the-Middle attack in an isolated Kathara virtual network using Python and Scapy to demonstrate ARP cache poisoning, unencrypted HTTP/TCP traffic interception, and switch-level countermeasures such as Dynamic ARP Inspection (DAI).
2. **[Network Reconnaissance and Port Scanning Analysis](./projects/nmap-service-scan/)**
   Conducted authorized active reconnaissance against a local lab target by combining Nmap service enumeration with a custom Python port scanner (`scanner.py`), cross-validating structured XML/JSON outputs and proposing host-hardening remediations.

---

## 5. Learning Journey

Transitioning from an undergraduate Computer Science background into dedicated postgraduate cybersecurity studies in **WQE7001 Cyber Security** has fundamentally shifted how I evaluate software and network systems. Previously, I focused primarily on whether code functioned correctly under expected inputs; this course trained me to think adversarially about trust boundaries, protocol assumptions, and defense-in-depth.

Two technical areas from the course stood out in shaping my practical understanding. First, exploring **network reconnaissance and service enumeration** demonstrated how much actionable intelligence an attacker can gather simply by fingerprinting open ports and outdated service banners. Combining Nmap with custom Python scanning logic showed me how automated discovery works under the hood and why minimizing exposed attack surfaces is essential. Second, studying **Layer-2 protocol vulnerabilities and traffic interception** in virtualized labs highlighted that protocols like ARP prioritize efficiency over authentication. Seeing cleartext traffic intercepted in a controlled environment reinforced why end-to-end encryption (TLS) and switch-level protections are non-negotiable in modern architectures.

Hands-on lab work also taught me valuable troubleshooting discipline. During my Kathara ARP spoofing lab, I initially encountered a connectivity blackout where victim nodes (`pc1` and `pc2`) lost all communication with each other as soon as spoofed ARP replies were transmitted. Instead of relaying traffic transparently, my attack turned into an unintended Denial of Service. By inspecting interface counters and kernel parameters inside the container using `tcpdump` and `sysctl`, I diagnosed that IPv4 packet forwarding (`net.ipv4.ip_forward`) was disabled on the intercepting node. Enabling IP forwarding immediately restored end-to-end packet flow while allowing passive traffic capture to succeed.

Despite strong progress in network scripting, **low-level memory safety and binary exploitation**—specifically analyzing stack/heap corruption and crafting reliable mitigations in legacy C/C++ codebases—remains a challenging area that requires deeper practice with debuggers and fuzzing tools.

To address this gap and prepare for advanced coursework, I have set a concrete improvement goal: **by February 28, 2027**, I will complete at least **10 hands-on memory corruption and secure coding challenges** on pwn.college or TryHackMe, and publish **two detailed vulnerability remediation write-ups** in this portfolio repository. Progress will be measured through verified lab completions and documented code patches demonstrating bounds checking and compiler-level mitigations.

---

## 6. Career Objective

My career objective after completing my Master of Cyber Security at Universiti Malaya is to become a **Security Software Engineer (Application Security Developer)**, combining my computer science programming foundation with offensive and defensive security expertise to build secure-by-design applications and automated security tooling.

To achieve this role, I will execute three concrete steps over the next twelve months:
1. **Master Secure Programming & Cryptography:** Excel in upcoming postgraduate modules including *Advanced Network Security Programming (WQE7002)* and *Cryptography and Information Hiding (WQE7003)*, applying secure coding principles to all academic software projects.
2. **Build Open-Source Security Tools:** Expand this GitHub portfolio with automated vulnerability scanning, static analysis, and packet-inspection tools written in Python and Go.
3. **Validate Baseline Security Credentials:** Complete the *ISC2 Certified in Cybersecurity (CC)* certification by March 2027 and pursue a security engineering internship prior to graduation.

---

## 7. Contact Information

* **Email:** 25122354@siswa.um.edu.my
* **GitHub:** [github.com/DuJerry](https://github.com/DuJerry)
* **LinkedIn:** https://www.linkedin.com/in/juan-du-aa945a441/
