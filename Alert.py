import time
import psutil
import os
import requests
from collections import deque

# =========================
# CONFIG
# =========================

LOG_FILE = "/var/log/auth.log"
THRESHOLD_FAILED_LOGINS = 5
TIME_WINDOW = 60  # seconds

SUSPICIOUS_PORTS = [22, 23, 3389, 4444, 5555]

# Telegram (اختياري)
ENABLE_TELEGRAM = False
BOT_TOKEN = "PUT_TOKEN_HERE"
CHAT_ID = "PUT_CHAT_ID_HERE"

# =========================
# STATE
# =========================

failed_attempts = deque()

# =========================
# ALERT SYSTEM
# =========================

def send_alert(message):
    print(f"\n🚨 ALERT: {message}\n")

    if ENABLE_TELEGRAM:
        try:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            requests.post(url, data={"chat_id": CHAT_ID, "text": message})
        except:
            print("⚠️ Telegram alert failed")

# =========================
# LOG MONITOR (BRUTE FORCE)
# =========================

def monitor_logs():
    if not os.path.exists(LOG_FILE):
        return

    with open(LOG_FILE, "r") as f:
        f.seek(0, os.SEEK_END)

        while True:
            line = f.readline()
            if not line:
                break

            if "Failed password" in line:
                now = time.time()
                failed_attempts.append(now)

                # remove old entries
                while failed_attempts and now - failed_attempts[0] > TIME_WINDOW:
                    failed_attempts.popleft()

                if len(failed_attempts) >= THRESHOLD_FAILED_LOGINS:
                    send_alert(f"Brute force detected: {len(failed_attempts)} attempts")
                    failed_attempts.clear()

# =========================
# NETWORK MONITOR
# =========================

def monitor_network():
    for conn in psutil.net_connections(kind="inet"):
        if conn.status == "ESTABLISHED":

            local_port = conn.laddr.port if conn.laddr else None
            remote_ip = conn.raddr.ip if conn.raddr else None

            if local_port in SUSPICIOUS_PORTS:
                send_alert(f"Suspicious connection on port {local_port} from {remote_ip}")

# =========================
# MAIN LOOP
# =========================

def run_ids():
    print("🛡️ IDS System Started...\n")

    while True:
        try:
            monitor_logs()
            monitor_network()
            time.sleep(5)

        except KeyboardInterrupt:
            print("\nStopped by user.")
            break

        except Exception as e:
            print(f"Error: {e}")

# =========================
# START
# =========================

if __name__ == "__main__":
    run_ids()
