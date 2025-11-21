import os
import yaml

def generate_ovpn(client_name, server_ip, port, proto, password=None):
    os.makedirs("examples", exist_ok=True)
    ovpn_file = f"examples/{client_name}.ovpn"
    with open(ovpn_file, "w") as f:
        f.write(f"client\n")
        f.write(f"dev tun\n")
        f.write(f"proto {proto}\n")
        f.write(f"remote {server_ip} {port}\n")
        f.write(f"resolv-retry infinite\n")
        f.write(f"nobind\n")
        if password:
            f.write(f"auth-user-pass\n")
        f.write(f"<ca>\n# Certificado fictício\n</ca>\n")
        f.write(f"<cert>\n# Certificado {client_name}\n</cert>\n")
        f.write(f"<key>\n# Chave {client_name}\n</key>\n")
    print(f"[Simulação] Perfil .ovpn criado: {ovpn_file}")

if __name__ == "__main__":
    clients = [{"name": "clientA"}, {"name": "clientB"}]
    server_ip = "10.0.0.1"
    port = 1194
    proto = "udp"
    for c in clients:
        generate_ovpn(c["name"], server_ip, port, proto, password="secret123")
