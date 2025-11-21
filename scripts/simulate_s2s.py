from simulate_openvpn import simulate_openvpn_server
from simulate_ipsec import simulate_ipsec
from simulate_pfsense import simulate_device

def run_lab():
    simulate_device("pf1")
    simulate_device("pf2")
    simulate_openvpn_server("pf1")
    simulate_ipsec("pf1")
    simulate_ipsec("pf2")
    print("\n🏁 Simulação do laboratório completa!")

if __name__ == "__main__":
    run_lab()
