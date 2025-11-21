import time

firewall_logs = []
openvpn_logs = []
ipsec_logs = []

def log_firewall(msg):
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
    firewall_logs.append(f"{timestamp} - {msg}")

def log_openvpn(msg):
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
    openvpn_logs.append(f"{timestamp} - {msg}")

def log_ipsec(msg):
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
    ipsec_logs.append(f"{timestamp} - {msg}")
