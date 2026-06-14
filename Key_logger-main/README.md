# 🔍 Keylogging & Email Exfiltration Simulation 
## ⚠ Disclaimer

This project is developed strictly for **educational purposes in a controlled lab environment**.

It demonstrates how keystroke logging and data exfiltration techniques work so that cybersecurity professionals can understand, detect, and defend against them.

Do NOT deploy this on any system without explicit authorization.

---

## 📌 Overview

This project simulates how a basic keylogging mechanism can capture keyboard input and transmit collected data using SMTP email services.

The purpose of this project is to:

- Understand how keyloggers function internally
- Learn about data exfiltration techniques
- Study SMTP-based data transmission
- Improve defensive security awareness

---


---

## 🧠 How It Works (High-Level Explanation)

### 1️⃣ keylogger.py
- Captures keyboard input
- Stores logged keystrokes temporarily
- Sends collected data at fixed intervals

### 2️⃣ zlogger.py
- Imports the keylogger module
- Configures email credentials
- Initializes logging process
- Sends captured logs every 2 minutes via SMTP

---

## ⚙ Technologies Used

- Python
- SMTP (Simple Mail Transfer Protocol)
- Email Authentication (App Password)
- Time-based execution

---

## 📡 Data Transmission

Logs are sent at regular 2-minute intervals using SMTP email service.

This demonstrates how attackers may use:
- Legitimate email services
- Encrypted channels
- Scheduled data exfiltration

Understanding this helps in detecting abnormal outbound traffic.

---

## 🎯 Learning Objectives

Through this project, you gain knowledge of:

- Keyboard event handling in Python
- Modular code structure
- Scheduled execution
- SMTP email automation
- Data exfiltration concepts
- Real-world post-exploitation behavior

---

## 🛡 Defensive Awareness

To protect against such attacks:

- Use Endpoint Detection & Response (EDR)
- Monitor abnormal outbound email traffic
- Restrict background application permissions
- Enable multi-factor authentication
- Use antivirus with behavioral detection
- Monitor suspicious Python processes

---

## 🚨 Security Note

Modern operating systems and security tools often detect keylogging behavior.  
This project is meant for isolated virtual lab environments only.

---

## 👨‍💻 Author

Himanshu  
Cybersecurity Enthusiast | Python Developer | Ethical Hacking Learner

