import time
from firewall_sim import FirewallSim
from simulate_openvpn import OpenVPNSim
from simulate_ipsec import IPSecSim

print("\n📡 Iniciando simulação do pfSense: pf1")
time.sleep(0.2)
print("[pf1] Sistema iniciado ✓")

print("📡 Iniciando simulação do pfSense: pf2")
time.sleep(0.2)
print("[pf2] Sistema iniciado ✓")

# --------------------------------------------------
# 1) Instanciar Firewall
# --------------------------------------------------
fw = FirewallSim(device="pf1-firewall")

fw.add_rule("ALLOW", "10.8.0.0/24", "192.168.1.10", 22, "tcp", "SSH para servidor interno")
fw.add_rule("DENY", "any", "192.168.1.0/24", 3389, "tcp", "Bloquear RDP para LAN1")
fw.add_rule("ALLOW", "10.8.0.0/24", "192.168.1.0/24", "any", "any", "OpenVPN LAN access")
fw.add_rule("ALLOW", "10.9.0.0/24", "10.8.0.0/24", "any", "any", "Inter-VPN access")
fw.add_rule("ALLOW", "192.168.1.0/24", "192.168.50.0/24", "any", "any", "IPsec site-to-site")

fw.print_rules()

# --------------------------------------------------
# 2) Iniciar OpenVPN com múltiplos clientes/sub-redes
# --------------------------------------------------
print("📡 Iniciando OpenVPN server (simulado) em pf1...")

vpn = OpenVPNSim(server_name="pf1", subnet="10.8.0.0/24")
clients = ["clientA", "clientB", "clientC", "clientX"]

vpn_clients = vpn.connect_multiple(clients)

print("🏁 OpenVPN simulada ✓")

# --------------------------------------------------
# 3) Iniciar IPsec entre pf1 ↔ pf2
# --------------------------------------------------
print("📡 Configurando túnel IPsec (simulado) pf1 ↔ pf2")

ipsec = IPSecSim("pf1", "pf2")
ipsec_status = ipsec.establish_tunnel()

print("🏁 IPsec iniciada ✓")

# --------------------------------------------------
# 4) Simular Tráfego
# --------------------------------------------------
print("\n🔎 Testes de Tráfego & Políticas\n")

packets = [
    # VPN → LAN1
    {"src": vpn_clients["clientA"], "dst": "192.168.1.10", "port": 22, "proto": "tcp"},
    {"src": vpn_clients["clientB"], "dst": "192.168.1.25", "port": 80, "proto": "tcp"},

    # VPN → LAN1 (bloqueado RDP)
    {"src": vpn_clients["clientC"], "dst": "192.168.1.50", "port": 3389, "proto": "tcp"},

    # WAN → LAN1 (default deny)
    {"src": "172.16.0.10", "dst": "192.168.1.10", "port": 22, "proto": "tcp"},

    # LAN1 ↔ LAN2 via IPsec
    {"src": "192.168.1.10", "dst": "192.168.50.20", "port": 443, "proto": "tcp"},

    # Inter-VPN traffic
    {"src": "10.9.0.5", "dst": vpn_clients["clientA"], "port": 1234, "proto": "udp"},
]

results = fw.simulate_traffic(packets)

for pkt, decision in results:
    print(f"Pkt {pkt['src']} → {pkt['dst']}:{pkt['port']} [{pkt['proto'].upper()}]  →  {decision}")

# --------------------------------------------------
# 5) Logs Detalhados
# --------------------------------------------------
print("\n[ 📜 FIREWALL LOGS ]")
fw.print_logs()

print("\n[ 📜 OPENVPN LOGS ]")
vpn.print_logs()

print("\n[ 📜 IPSEC LOGS ]")
ipsec.print_logs()

print("\n🏁 Simulação completa do laboratório pfSense + VPNs concluída!")
