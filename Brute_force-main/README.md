# 🔐 Python Brute Force Login Tester

## ⚠ Disclaimer
This project is created strictly for **educational and authorized penetration testing purposes only**.  
Do NOT use this tool on websites or systems without explicit permission. Unauthorized use is illegal.

---

## 📌 Overview

This is a basic Python brute force login testing script.

The script:
- Takes a target login URL
- Uses correct form field names (from Inspect Element)
- Reads passwords from a dictionary file (`password.txt`)
- Attempts login until a valid password is found

This project is built to understand:
- Authentication testing
- Weak password detection
- HTTP request automation
- How brute force attacks work in controlled lab environments

---


---

## ⚡ Limitations

This basic script will NOT work against:

- CAPTCHA protected forms
- CSRF token protected forms
- Rate limited systems
- Multi-Factor Authentication (MFA)
- Account lockout mechanisms

Modern applications block brute force attempts.

---

## 🧠 Learning Outcomes

By building this project, you understand:

- HTTP POST requests
- Form data submission
- Dictionary-based password attacks
- Response analysis
- Basic web authentication flow

---

## 🔐 Defensive Measures (How to Prevent Brute Force)

- Implement rate limiting
- Enable account lockout after failed attempts
- Use CAPTCHA
- Enforce strong password policies
- Enable Multi-Factor Authentication (MFA)

---

## 👨‍💻 Author

Himanshu  
Cybersecurity Enthusiast | Python Developer | Ethical Hacking Learner

