import time
import os

def log(device, message):
    os.makedirs(f"{device}/logs", exist_ok=True)
    with open(f"{device}/logs/system.log", "a") as f:
        f.write(f"{time.ctime()} - {message}\n")

def vpn_log(device, message):
    os.makedirs(f"{device}/logs", exist_ok=True)
    with open(f"{device}/logs/vpn.log", "a") as f:
        f.write(f"{time.ctime()} - {message}\n")
