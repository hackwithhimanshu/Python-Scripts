# 🌐 DNS Spoofing Simulation (Lab Research Project)

## ⚠ Disclaimer
This project is strictly for educational use in an isolated lab environment.  
Do NOT deploy or test on networks without explicit authorization.

---

## 📌 Overview

This project demonstrates how DNS spoofing works at a conceptual level using packet interception and modification techniques.

It simulates how a malicious actor could:
- Intercept DNS responses
- Modify DNS answer records
- Redirect traffic to a different IP address

The purpose of this project is to understand:
- DNS packet structure
- Packet interception
- Man-in-the-Middle (MITM) concepts
- How attackers manipulate DNS responses
- How defenders detect and prevent such attacks

---

## 📂 Project Structure

dns-spoof/
│
├── dns_spoof.py
└── README.md

---

## 🛠 Technologies Used

- Python
- Scapy (packet manipulation)
- NetfilterQueue (packet interception)
- Linux networking stack

---

## ⚙ How It Works (High-Level)

1. Captures network packets from the queue.
2. Checks if packet contains a DNS response layer.
3. If the queried domain matches a target:
   - Replaces the DNS answer with a custom IP address.
4. Recalculates packet length and checksums.
5. Sends modified packet back into the network stream.

This demonstrates how DNS responses can be manipulated in a Man-in-the-Middle scenario.

---

## 🎯 Learning Outcomes

By building this project, you understand:

- DNS request and response structure
- IP and UDP packet fields
- Checksum recalculation
- Traffic interception in Linux
- DNS-based redirection attacks
- Post-exploitation network manipulation

---

## ⚡ Limitations

- Works only in controlled lab networks
- Requires Linux environment
- Requires administrative/root privileges
- Modern networks may block or detect spoofing attempts
- Does not bypass DNSSEC

---

## 🛡 Defensive Measures Against DNS Spoofing

To protect networks:

- Use DNSSEC
- Enable HTTPS and HSTS
- Monitor ARP and DNS anomalies
- Deploy IDS/IPS systems
- Use encrypted DNS (DoH / DoT)
- Implement network segmentation

---

## 🔐 Security Awareness

DNS spoofing is a real-world attack technique used in phishing, redirection, and credential theft campaigns.  
Understanding this attack helps security professionals build stronger defenses.

---

## 👨‍💻 Author

Himanshu  
Cybersecurity Enthusiast | Python Developer | Ethical Hacking Learner
