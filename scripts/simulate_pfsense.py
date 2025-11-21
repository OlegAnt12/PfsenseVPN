import os
from simulate_log import log

def simulate_device(device_path):
    print(f"\n📡 Iniciando simulação do pfSense: {device_path}")
    log(device_path, "pfSense iniciado")
    print(f"[{device_path}] Sistema iniciado ✓")

if __name__ == "__main__":
    simulate_device("pf1")
    simulate_device("pf2")
