import yaml
import time
from simulate_log import vpn_log

def load_config(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def simulate_openvpn_server(device_path):
    cfg = load_config(f"{device_path}/config/vpn_openvpn.yml")
    if not cfg["enabled"]:
        print(f"[{device_path}] OpenVPN desativado")
        return

    print(f"[{device_path}] Iniciando OpenVPN server {cfg['server']['ip']}:{cfg['server']['port']}")
    vpn_log(device_path, "OpenVPN server iniciado")

    for client in cfg.get("clients", []):
        time.sleep(0.5)
        print(f"[{device_path}] Cliente {client['name']} conectado → IP {client['ip']}")
        vpn_log(device_path, f"Cliente {client['name']} conectado com IP {client['ip']}")
        client_file = f"{device_path}/config/{client['name']}_status.yml"
        with open(client_file, "w") as f:
            f.write(f"connected: true\nip: {client['ip']}\n")

if __name__ == "__main__":
    simulate_openvpn_server("pf1")
