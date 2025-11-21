import os
import yaml
import time

# Função para gerar arquivo .ovpn
def generate_ovpn(client_name, server_ip="10.0.0.1", port=1194, proto="udp", auth="password"):
    os.makedirs("examples", exist_ok=True)
    ovpn_path = f"examples/{client_name}.ovpn"
    
    with open(ovpn_path, "w") as f:
        f.write(f"client\n")
        f.write(f"dev tun\n")
        f.write(f"proto {proto}\n")
        f.write(f"remote {server_ip} {port}\n")
        f.write(f"resolv-retry infinite\n")
        f.write(f"nobind\n")
        if auth == "password":
            f.write(f"auth-user-pass\n")
        f.write(f"<ca>\n# Certificado fictício do CA\n</ca>\n")
        f.write(f"<cert>\n# Certificado do cliente {client_name}\n</cert>\n")
        f.write(f"<key>\n# Chave privada do cliente {client_name}\n</key>\n")
    print(f"[Simulação] Perfil .ovpn gerado: {ovpn_path}")
    return ovpn_path

# Função para atualizar status do cliente
def update_status(client_name, ip="10.8.0.0", connected=True):
    os.makedirs("pf1/config", exist_ok=True)
    status_file = f"pf1/config/{client_name}_status.yml"
    status_data = {
        "connected": connected,
        "ip": ip
    }
    with open(status_file, "w") as f:
        yaml.dump(status_data, f)
    print(f"[Simulação] Status atualizado: {status_file}")

# Função principal de simulação
def simulate_openvpn():
    clients = [
        {"name": "clientA", "ip": "10.8.0.2", "auth": "password"},
        {"name": "clientB", "ip": "10.8.0.3", "auth": "certificate"}
    ]
    server_ip = "10.0.0.1"
    port = 1194
    proto = "udp"

    print("📡 Iniciando OpenVPN server (simulado)...")
    time.sleep(1)

    for c in clients:
        generate_ovpn(c["name"], server_ip, port, proto, c["auth"])
        update_status(c["name"], c["ip"], connected=True)
        print(f"[Simulação] Cliente {c['name']} conectado → IP {c['ip']}")
        time.sleep(0.5)

    print("🏁 Simulação OpenVPN completa!")


if __name__ == "__main__":
    simulate_openvpn()
