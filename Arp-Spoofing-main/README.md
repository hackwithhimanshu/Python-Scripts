# 🛡️ ARP Spoofing — Practical Guide & Detection

This repository demonstrates how ARP spoofing works inside a local network and how it can be detected.  
The purpose of this project is **education, awareness, and cybersecurity learning**.

---

# 📂 Scripts Included

## 1️⃣ arp_spoof.py
This script demonstrates ARP spoofing inside a shared network (lab use only).

Before running, update two values inside the script:

- Victim IP → Target device
- Gateway IP → Router address

### Example
- Victim IP = "192.168.25.34"
- Gateway IP = "192.168.25.1"


The script sends crafted ARP replies to position the attacker between victim and router.

---

## 2️⃣ arp_spoof_detector.py
This script checks whether your machine might be affected by ARP spoofing.

### What it does:
- Scans ARP table
- Verifies MAC address consistency
- Alerts on suspicious gateway behavior

Use this script to understand defensive monitoring concepts.

---

# 📘 ARP Spoofing Overview

## 🔎 What is ARP Spoofing?
ARP Spoofing is a technique where fake ARP responses are sent inside a shared network.

The attacker pretends to be:
- The router
- Another device

Since ARP has no authentication, devices trust these fake replies and redirect traffic through the attacker.

---

## 🌐 When Can ARP Spoofing Happen?
Usually inside shared networks:

- Same Wi-Fi router
- College or office LAN
- Public hotspot
- Home network with multiple devices

Anyone connected to the same router can attempt ARP manipulation.

---

## ⚙️ How the Attack Works (Simple Flow)

1. Victim and router communicate normally.
2. Attacker joins the same network.
3. Attacker sends fake ARP replies:
   - Router IP → Attacker MAC
   - Victim IP → Attacker MAC
4. Traffic starts flowing through the attacker.

This creates a **Man-in-the-Middle (MITM)** position.

---

## 👁️ What Can an Attacker Do?
If traffic passes through the attacker, they may:

- Read network requests
- Monitor browsing activity
- Capture login data on insecure sites
- Modify or redirect packets
- Inject malicious content (advanced setups)

⚠️ HTTPS reduces risk but does not make attacks impossible.

---

## ❓ Why ARP Spoofing Works
ARP is an old protocol built for trusted networks. It does not:

- Verify sender identity
- Authenticate ARP replies
- Use encryption

Devices simply trust the latest ARP response they receive.

---

## 🚨 Possible Warning Signs

- Slow internet suddenly
- Random disconnections
- SSL or certificate warnings
- Duplicate IP/MAC alerts
- Gateway MAC address changing

---

## 🔐 Basic Protection Methods

- Use HTTPS whenever possible
- Avoid sensitive logins on public Wi-Fi
- Use VPN for extra protection
- Monitor ARP tables
- Enable switch security features
- Use static ARP entries in controlled networks

---

## 🎓 Educational Purpose
This project is created for cybersecurity learning:

- Understanding local network attacks
- Learning MITM concepts
- Practicing ethical hacking in lab environments
- Building strong networking fundamentals

---

## ✅ Key Takeaway
ARP spoofing is not remote internet hacking.  
It happens when devices share the same network and trust fake ARP messages.

Understanding ARP trust helps you understand how local MITM attacks become possible.

---

⚠️ **Disclaimer:**  
Use these scripts only in environments where you have permission.  
Unauthorized use on real networks may be illegal.
