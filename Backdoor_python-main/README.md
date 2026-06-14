# 🔐 Python Reverse Backdoor (Educational Project)

> ⚠️ DISCLAIMER  
> This project is created strictly for educational and ethical hacking practice in controlled lab environments. Do NOT use this on systems without proper authorization. Unauthorized access to computer systems is illegal.

---

## 📌 Overview

This project demonstrates a basic **Python Reverse Backdoor** using socket programming.

It consists of two main components:

- `listener.py` → Runs on the attacker machine  
- `reverse_backdoor.py` → Runs on the target machine  

When `reverse_backdoor.py` is executed on the target system, it initiates a connection back to the attacker machine. Once connected, the attacker gains remote command execution access.

This project helps in understanding how reverse shells work in real-world attack scenarios and why defensive security mechanisms are important.

---

## ⚙️ Features

After a successful connection, the attacker can:

- Navigate directories on the target system
- Execute system commands remotely
- Download files from the target machine
- Upload files to the target machine

---

## 🛠️ Technologies Used

- Python 3
- Socket Programming
- OS & Subprocess modules

---

## 🧠 How It Works

1. The attacker starts `listener.py`.
2. The script waits for an incoming connection.
3. The target executes `reverse_backdoor.py`.
4. The target machine connects back to the attacker.
5. A remote shell session is established.
6. The attacker can now send commands to the target system.

This follows the **reverse shell model**, where the connection is initiated by the victim machine.

---

## 🚀 Setup & Usage (Lab Environment Only)

### Step 1 – Configure IP & Port

Edit `reverse_backdoor.py` and replace with your attacker machine IP:

```python
SERVER_IP = "YOUR_IP_ADDRESS"
PORT = 4444
```

### Step 2 – Start Listener (Attacker Machine)
```python
python listener.py
```

### Step 3 – Execute Backdoor (Target Machine)
```python
python reverse_backdoor.py
```

