# 🌐 Subdomain Crawler (Python)

## ⚠ Disclaimer

This tool is developed for **educational and authorized security testing purposes only**.  
Do NOT scan domains without proper permission. Unauthorized reconnaissance may be illegal.

---

## 📌 Overview

This is a basic Python-based Subdomain Crawler.

It works by:
- Taking a target domain
- Reading possible subdomain names from a wordlist file
- Sending HTTP requests using the `requests` library
- Checking for **HTTP 200 responses**
- Printing discovered subdomains

This project helps in understanding basic reconnaissance techniques used during security assessments.

---
## ⚙ How It Works

1. User enters the target domain (example: example.com)
2. Script reads subdomains from `subdomains-wordlist.txt`
3. For each keyword:
   - It constructs: `keyword.targetdomain.com`
   - Sends HTTP request
   - If response status is **200**, it prints:

```python
[+] Discovered Subdomain: http://subdomain.target.com
```


---

## ⚡ Limitations

- Only detects subdomains returning HTTP 200
- Does not detect:
  - Wildcard DNS setups
  - Hidden or private subdomains
  - Rate-limited responses
- No threading (basic sequential scanning)

---

## 🎯 Learning Outcomes

By building this project, you understand:

- HTTP requests using Python
- Wordlist-based enumeration
- Basic reconnaissance methodology
- Response status code handling
- Automation in security testing

---

## 🛡 Defensive Measures

To protect your domain from subdomain enumeration:

- Avoid exposing unnecessary subdomains
- Disable unused services
- Monitor abnormal traffic
- Use Web Application Firewalls (WAF)
- Implement rate limiting

---

## 👨‍💻 Author

Himanshu  
Cybersecurity Enthusiast | Python Developer | Ethical Hacking Learner


