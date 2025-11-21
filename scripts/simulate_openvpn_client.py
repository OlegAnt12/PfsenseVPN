import yaml
import time
from simulate_log import vpn_log

def connect_to_server(client_name, server_device, ip):
    print(f"[{client_name}] Tentando conectar ao OpenVPN server {server_device}")
    time.sleep(0.5)
    print(f"[{client_name}] Conectado com IP {ip}")
    vpn_log(server_device, f"{client_name} estabeleceu conexão VPN")
    return True

if __name__ == "__main__":
    clients = [
        {"name": "clientA", "server": "pf1", "ip": "10.8.0.2"},
        {"name": "clientB", "server": "pf1", "ip": "10.8.0.3"},
    ]

    for c in clients:
        connect_to_server(c["name"], c["server"], c["ip"])
