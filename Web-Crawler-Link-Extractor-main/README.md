# 🕷 Web Crawler & Link Extractor (Spider)

## ⚠ Disclaimer
This tool is created strictly for educational purposes and authorized security testing only.  
Do NOT crawl websites without permission.

---

## 📌 Overview

This is a basic Python-based Web Crawler (Spider).

The script:
- Starts from a target URL
- Extracts links from HTML pages
- Normalizes links using urljoin
- Recursively crawls internal links
- Prints discovered URLs

This project helps understand how search engines and security tools discover pages inside a website.

---

## 📂 Project Structure

web-spider/
│
├── spider.py
└── README.md

---

## 🛠 Technologies Used

- Python
- requests (HTTP requests)
- re (Regular Expressions)
- urllib.parse (URL normalization)

Install dependency:

pip install requests

---

## ⚙ How It Works

1. Target URL is defined inside the script.
2. Sends HTTP request to fetch page content.
3. Extracts links using regex pattern matching.
4. Converts relative URLs into absolute URLs using urljoin.
5. Removes fragment identifiers (#).
6. Avoids duplicate links.
7. Recursively crawls internal links.

---

## 🚀 Usage

1. Modify the target URL inside spider.py:

target_url = "http://example.com/"

2. Run the script:

python spider.py

The crawler will print all discovered internal links.

---

## 🎯 Learning Outcomes

By building this project, you understand:

- Recursive crawling logic
- Link extraction techniques
- URL normalization
- Basic website structure mapping
- Automation in reconnaissance

---

## ⚡ Limitations

- Uses basic regex for link extraction
- No depth control
- No threading (slow on large sites)
- No robots.txt handling
- No rate limiting
- Only crawls links containing the base target URL

---

## 🛡 Defensive Awareness

To protect against aggressive crawling:

- Implement rate limiting
- Use robots.txt
- Deploy Web Application Firewall (WAF)
- Monitor abnormal request patterns
- Block automated bots if necessary

---

## 🔐 Security Insight

Web crawling is a fundamental technique used by:

- Search engines
- Security scanners
- Bug bounty hunters
- Reconnaissance tools

Understanding crawling helps security professionals both discover exposures and defend against automated mapping.

---

## 👨‍💻 Author

Himanshu  
Cybersecurity Enthusiast | Python Developer | Ethical Hacking Learner
