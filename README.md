# 🛡️ Intrusion-Alert-Educational-Network-IDS

A lightweight Intrusion Detection System (IDS) built with Python to monitor network traffic and detect potential DoS/DDoS attacks based on request rate per IP.

---

## 📌 Features

* 📡 Real-time packet sniffing using Scapy
* 📊 Tracks number of requests per IP address
* 🚨 Detects potential DoS/DDoS attacks
* 🪟 GUI alert system using Tkinter
* ⚡ Multi-threaded for better performance

---

## 🧠 How It Works

1. The script listens to all incoming IP packets.
2. Each packet source IP is tracked.
3. Requests are counted per second.
4. If a specific IP exceeds the threshold (default: 100 requests/sec), an alert is triggered.

---

## ⚙️ Requirements

Make sure you have Python 3 installed, then install dependencies:

```bash
pip install scapy
```

> ⚠️ Note: You may need administrative/root privileges to sniff network traffic.

---

## ▶️ Usage

Run the script:

```bash
sudo python plugin.py
```

(Use `sudo` on Linux/macOS for packet sniffing permissions)

---

## 🔧 Configuration

You can adjust detection sensitivity by modifying:

```python
THRESHOLD = 100  # Requests per second
```

---

## 🚨 Alert System

* Displays a popup window when suspicious activity is detected
* Prints alert message in the terminal

Example:

```
Possible DDoS/DoS attack detected!
Source IP: 192.168.1.5
```

---

## ⚠️ Limitations

* May produce false positives (e.g. high traffic like downloads or streaming)
* Detects only based on packet rate (not protocol-specific attacks)
* GUI alerts may cause performance issues if triggered frequently
* Requires root/admin privileges

---

## 💡 Future Improvements

* Detect specific attack types (SYN Flood, UDP Flood)
* Add logging system instead of GUI alerts
* Integrate with firewall to block malicious IPs
* Web dashboard for monitoring
* Port-based filtering

---

## 📂 Project Structure

```
.
├── ids.py
└── README.md
```

---

## 👨‍💻 Author

Belal Eladawy
Network Engineer & Security Researcher

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ⭐ Support

If you find this project useful, consider giving it a star ⭐ on GitHub!


---


