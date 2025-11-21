# simulate_s2s.py
import time
from firewall_sim import FirewallSim
from simulate_openvpn import OpenVPNSim
from simulate_ipsec import IPSecSim

# Função central para rodar todo o laboratório
def run_lab_simulation(
    start_firewall=True,
    start_openvpn=True,
    start_ipsec=True,
    simulate_traffic=False,
    show_logs=False
):
    print("\n📡 Iniciando simulação do pfSense: pf1")
    time.sleep(0.5)
    print("[pf1] Sistema iniciado ✓")
    print("📡 Iniciando simulação do pfSense: pf2")
    time.sleep(0.5)
    print("[pf2] Sistema iniciado ✓\n")

    # Inicializar Firewall
    fw = None
    if start_firewall:
        fw = FirewallSim()
        print("[ 🔥 FIREWALL RULES ]")
        fw.add_rule("ALLOW", "10.8.0.0/24", "192.168.1.10", 22, "tcp", "SSH para servidor interno")
        fw.add_rule("DENY", "any", "192.168.1.0/24", 3389, "tcp", "Bloquear RDP para LAN1")
        fw.add_rule("ALLOW", "any", "10.8.0.0/24", "any", "any", "OpenVPN LAN access")
        fw.add_rule("ALLOW", "any", "10.9.0.0/24", "10.8.0.0/24", "any", "Inter-VPN access")
        fw.add_rule("ALLOW", "any", "192.168.1.0/24", "192.168.50.0/24", "any", "IPsec site-to-site")
        fw.print_rules()
        print()

    # Inicializar OpenVPN
    openvpn = None
    if start_openvpn:
        openvpn = OpenVPNSim()
        print("📡 Iniciando OpenVPN server (simulado) em pf1...")
        openvpn.start()
        openvpn.print_logs()
        print("🏁 OpenVPN simulada ✓\n")

    # Inicializar IPsec
    ipsec = None
    if start_ipsec:
        ipsec = IPSecSim()
        print("📡 Configurando túnel IPsec (simulado) pf1 ↔ pf2")
        ipsec.establish_tunnel()
        ipsec.print_logs()
        print("🏁 IPsec simulada ✓\n")

    # Simular tráfego entre clientes e sub-redes
    results = []
    if simulate_traffic and fw:
        print("🔎 Testes de Tráfego")
        # Exemplo de pacotes simulados
        packets = [
            {"src": "10.8.0.2", "dst": "192.168.1.10", "port": 22, "proto": "tcp"},
            {"src": "10.8.0.3", "dst": "192.168.1.25", "port": 80, "proto": "tcp"},
            {"src": "10.8.0.4", "dst": "192.168.1.50", "port": 3389, "proto": "tcp"},
            {"src": "172.16.0.10", "dst": "192.168.1.10", "port": 22, "proto": "tcp"},
        ]
        for pkt in packets:
            decision = fw.evaluate_packet(pkt)
            results.append((pkt, decision))
            print(f"Pkt {pkt['src']} → {pkt['dst']}:{pkt['port']} [{pkt['proto'].upper()}]  →  {decision}")
        print()
        fw.print_logs()
        print()

    # Exibir logs completos se solicitado
    if show_logs:
        if openvpn:
            print("[ 📜 OPENVPN LOGS ]")
            openvpn.print_logs()
            print()
        if ipsec:
            print("[ 📜 IPSEC LOGS ]")
            ipsec.print_logs()
            print()

    return results

# Executar laboratório completo ao rodar este arquivo diretamente
if __name__ == "__main__":
    run_lab_simulation(
        start_firewall=True,
        start_openvpn=True,
        start_ipsec=True,
        simulate_traffic=True,
        show_logs=True
    )
