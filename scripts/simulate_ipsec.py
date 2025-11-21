import yaml
import time
from simulate_log import vpn_log

def load_config(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def simulate_ipsec(device_path):
    cfg = load_config(f"{device_path}/config/vpn_ipsec.yml")
    if not cfg["enabled"]:
        print(f"[{device_path}] IPsec desativado")
        return

    for tunnel in cfg.get("tunnels", []):
        time.sleep(0.5)
        print(f"[{device_path}] Túnel IPsec ativo com peer {tunnel['peer']}")
        vpn_log(device_path, f"Túnel IPsec com {tunnel['peer']} estabelecido")

if __name__ == "__main__":
    simulate_ipsec("pf1")
    simulate_ipsec("pf2")
