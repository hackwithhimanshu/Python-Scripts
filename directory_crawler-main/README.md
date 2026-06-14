# 📂 Directory Crawler (Python)

## ⚠ Disclaimer
This tool is created strictly for educational purposes and authorized security testing only.  
Do NOT scan websites without proper permission.

---

## 📌 Overview
This is a basic Python-based Directory Crawler.

The script:
- Takes a target URL
- Reads directory names from a wordlist file
- Sends HTTP GET requests using the `requests` library
- Prints discovered directories when a valid response is received

This technique is commonly used in the reconnaissance phase of penetration testing.

---

## 📂 Project Structure

directory-crawler/
│
├── directory_crawler.py
├── files-and-dirs-wordlist.txt
└── README.md

---

## 🛠 Requirements

Install dependency:

pip install requests

---

## 📝 Wordlist Format

Create a file named:

files-and-dirs-wordlist.txt

Example:

admin
login
uploads
config
backup
images
test

Each directory name must be on a new line.

---

## ⚙ How It Works

1. Target URL is defined inside the script.
2. Script reads directory names from the wordlist.
3. For each word:
   - It appends the word to the target URL.
   - Sends a GET request.
4. If the server responds successfully, it prints:

[+] Discovered URL --> http://target/directory

---

## 🚀 Usage

1. Modify the target_url variable inside the script:

target_url = "http://example.com/"

2. Run the script:

python directory_crawler.py

---

## 🎯 Learning Outcomes

By building this project, you understand:

- HTTP requests in Python
- Wordlist-based enumeration
- Web reconnaissance basics
- Response handling
- Automation in security testing

---

## ⚡ Limitations

- Sequential scanning (no threading)
- No status code filtering
- No HTTPS handling (unless modified)
- No rate limit handling

---

## 🛡 Defensive Measures

To protect against directory enumeration:

- Disable directory listing
- Remove unused files
- Implement proper access control
- Use a Web Application Firewall (WAF)
- Monitor abnormal traffic patterns

---

## 👨‍💻 Author

Himanshu  
Cybersecurity Enthusiast | Python Developer | Ethical Hacking Learner
