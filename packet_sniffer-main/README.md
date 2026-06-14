# 📡 Packet Sniffer (HTTP Traffic Analysis - Lab Project)

## ⚠ Disclaimer
This project is strictly for educational use in a controlled lab environment.  
Do NOT capture network traffic on networks without proper authorization.

Unauthorized packet sniffing may violate privacy laws and security policies.

---

## 📌 Overview

This project demonstrates how packet sniffing works using Python and Scapy.

The script:
- Listens on a specified network interface
- Captures live packets
- Detects HTTP requests
- Extracts requested URLs
- Analyzes packet payloads for login-related patterns (lab demonstration)

The goal of this project is to understand how unencrypted HTTP traffic can expose sensitive information.

---

## 📂 Project Structure

packet-sniffer/
│
├── packet_sniffer.py
└── README.md

---

## 🛠 Technologies Used

- Python 3
- Scapy
- HTTP packet parsing
- Network interface monitoring

---

## ⚙ How It Works (High-Level)

1. Sniffs packets from a selected interface.
2. Checks whether a packet contains an HTTP request layer.
3. Extracts:
   - Host
   - Path
4. Prints full requested URL.
5. Inspects raw payload data for login-related keywords (educational demonstration).

This highlights the security risks of transmitting credentials over unencrypted HTTP.

---

## 🚀 Usage

Run with administrative privileges:

sudo python3 packet_sniffer.py

Make sure to update the interface name in the script if needed:

sniff("wlan0")

---

## 🖥 Example Output

[+] HTTP Request >> example.com/login  
[+] HTTP Request >> testsite.com/index.php  

---

## 🎯 Learning Outcomes

By building this project, you understand:

- How packet sniffing works
- Network layers (IP, TCP, HTTP)
- Packet filtering and parsing
- Risks of unencrypted traffic
- Basic network traffic inspection
- Credential exposure risks in HTTP

---

## ⚡ Limitations

- Only detects HTTP (not HTTPS encrypted traffic)
- Requires root/sudo privileges
- Works best in lab environments
- Does not decrypt TLS/SSL traffic

---

## 🛡 Defensive Awareness

To protect against packet sniffing attacks:

- Always use HTTPS
- Implement HSTS
- Use encrypted protocols (TLS)
- Avoid sending credentials over HTTP
- Use VPN on untrusted networks
- Deploy network intrusion detection systems (NIDS)

---

## 🔐 Security Insight

Modern web applications use HTTPS to prevent attackers from reading traffic in transit.  
This project demonstrates why encryption is critical for protecting user data.

---

## 👨‍💻 Author

Himanshu  
Cybersecurity Enthusiast | Python Developer | Ethical Hacking Learner
