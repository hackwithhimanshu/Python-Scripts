# 🔄 MAC Address Changer (Python)

## ⚠ Disclaimer
This tool is created strictly for educational purposes and authorized network testing only.  
Do NOT modify MAC addresses on networks you do not own or have permission to test.

---

## 📌 Overview

This is a Python-based MAC Address Changer for Linux systems.

The script:
- Takes a network interface as input
- Takes a new MAC address as input
- Brings the interface down
- Changes the MAC address
- Brings the interface back up
- Verifies whether the change was successful

This project helps understand how MAC address spoofing works at the system level.

---

## 📂 Project Structure

mac-changer/
│
├── mac_changer.py
└── README.md

---

## 🛠 Requirements

- Python 3
- Linux Operating System
- ifconfig installed
- Root/Sudo privileges

No external Python libraries are required.

---

## ⚙ How It Works

1. Parses command-line arguments using `optparse`.
2. Retrieves current MAC address using `ifconfig`.
3. Uses `subprocess` to:
   - Disable the network interface
   - Change MAC address
   - Enable the network interface
4. Verifies whether the MAC address was successfully changed.

---

## 🚀 Usage

Run with sudo privileges:

sudo python mac_changer.py -i <interface> -m <new_mac>

Example:

sudo python mac_changer.py -i eth0 -m 00:11:22:33:44:55

---

## 🖥 Example Output

Current MAC = 08:00:27:ab:cd:ef  
[+] Changing MAC Address for eth0 to 00:11:22:33:44:55  
[+] MAC Address was successfully changed to 00:11:22:33:44:55  

---

## 🎯 Learning Outcomes

By building this project, you understand:

- How MAC addresses work
- Network interface manipulation
- Subprocess execution in Python
- Regex for pattern extraction
- Command-line argument parsing
- Basic network spoofing concepts

---

## ⚡ Limitations

- Works only on Linux systems
- Requires sudo/root privileges
- Uses ifconfig (deprecated in some modern systems)
- Does not support Windows or macOS by default

---

## 🛡 Defensive Awareness

To detect MAC spoofing:

- Enable port security on switches
- Monitor ARP table inconsistencies
- Use Network Access Control (NAC)
- Log unexpected MAC address changes

---

## 👨‍💻 Author

Himanshu  
Cybersecurity Enthusiast | Python Developer | Ethical Hacking Learner
