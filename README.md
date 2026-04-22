
---

# 🛡️ Intrusion Detection System (IDS) - Python Script

## 📌 Overview

This project is a lightweight **Intrusion Detection System (IDS)** written in Python.
It monitors system login attempts and network connections in real-time to detect suspicious activity such as brute-force attacks and unusual port usage.

---

## ⚙️ Features

* 🔐 Monitors failed login attempts (`/var/log/auth.log`)
* 🚨 Detects brute-force attacks based on threshold & time window
* 🌐 Monitors active network connections
* ⚠️ Flags suspicious ports (e.g., 22, 23, 3389, 4444, 5555)
* 📢 Real-time alerts in terminal
* 📲 Optional Telegram notifications

---

## 🧰 Requirements

* Python 3.7+
* Linux system (Ubuntu/Debian recommended)
* Root or read access to system logs

### Install dependencies:

```bash
pip install psutil requests
```

---

## 🚀 Usage

1. Clone or copy the script:

```bash
git clone <repo-url>
cd ids-project
```

2. Run the script:

```bash
python3 ids.py
```

---

## ⚙️ Configuration

Edit these values inside the script:

```python
LOG_FILE = "/var/log/auth.log"
THRESHOLD_FAILED_LOGINS = 5
TIME_WINDOW = 60
SUSPICIOUS_PORTS = [22, 23, 3389, 4444, 5555]
```

### Telegram Alerts (Optional)

Enable Telegram alerts:

```python
ENABLE_TELEGRAM = True
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
```

---

## 📊 How It Works

### 1. Login Monitoring

Tracks failed login attempts.
If failures exceed threshold within a time window → alert triggered.

### 2. Network Monitoring

Scans active connections.
If suspicious ports are detected → alert triggered.

### 3. Alert System

Displays alerts in terminal and optionally sends Telegram messages.

---

## ⚠️ Disclaimer

This project is for **educational and research purposes only**.
Do not use it in unauthorized environments or against systems you do not own or have permission to monitor.

---

## 🔧 Future Improvements

* Auto IP blocking (iptables / ufw)
* Web dashboard (Flask / FastAPI)
* Machine learning anomaly detection
* Centralized logging system
* Email alert integration

---


