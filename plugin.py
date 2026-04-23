from scapy.all import sniff
import tkinter as tk
from collections import defaultdict
import time
import threading

# عدد الطلبات المسموح بها في الثانية
THRESHOLD = 100  
requests_count = defaultdict(int)

def show_alert(message):
    root = tk.Tk()
    root.title("Network Security Alert")
    root.geometry("400x150")
    label = tk.Label(root, text=message, font=("Arial", 14), fg="red")
    label.pack(pady=20)
    tk.Button(root, text="OK", command=root.destroy).pack()
    root.mainloop()

def reset_counter():
    while True:
        time.sleep(1)
        requests_count.clear()

def packet_callback(packet):
    if packet.haslayer("IP"):
        src = packet["IP"].src
        requests_count[src] += 1
        
        if requests_count[src] > THRESHOLD:
            alert = f"Possible DDoS/DoS attack detected!\nSource IP: {src}"
            print(alert)
            threading.Thread(target=show_alert, args=(alert,)).start()

# Thread لعداد كل ثانية
threading.Thread(target=reset_counter, daemon=True).start()

print("Monitoring network... Press CTRL+C to stop.")
sniff(filter="ip", prn=packet_callback, store=False)
