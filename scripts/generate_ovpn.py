import os

def generate_ovpn(client_name, server_ip="10.0.0.1", port=1194, proto="udp", auth="password"):
    """
    Gera um arquivo .ovpn simulado para um cliente
    """
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


if __name__ == "__main__":
    clients = ["clientA", "clientB"]
    for c in clients:
        generate_ovpn(c)
