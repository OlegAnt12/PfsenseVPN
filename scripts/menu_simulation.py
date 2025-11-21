# menu_simulation.py
import sys
from simulate_s2s import run_lab_simulation
from firewall_sim import FirewallSim
from simulate_openvpn import OpenVPNSim
from simulate_ipsec import IPSecSim

def main_menu():
    while True:
        print("\n===== LABORATÓRIO pfSense + VPNs =====")
        print("1. Simular pfSense básico")
        print("2. Simular OpenVPN (Remote Access)")
        print("3. Simular IPsec Site-to-Site")
        print("4. Simular tráfego entre sub-redes")
        print("5. Mostrar regras do firewall")
        print("6. Mostrar logs completos do laboratório")
        print("0. Sair")
        
        choice = input("Escolha uma opção: ").strip()

        if choice == "1":
            print("\n📡 Simulando pfSense básico...")
            run_lab_simulation(
                start_firewall=True,
                start_openvpn=False,
                start_ipsec=False,
                simulate_traffic=False,
                show_logs=False
            )
        elif choice == "2":
            print("\n📡 Simulando OpenVPN...")
            openvpn = OpenVPNSim()
            openvpn.start()
            openvpn.print_logs()
        elif choice == "3":
            print("\n📡 Simulando túnel IPsec site-to-site...")
            ipsec = IPSecSim()
            ipsec.establish_tunnel()
            ipsec.print_logs()
        elif choice == "4":
            print("\n🔎 Simulando tráfego entre sub-redes (OpenVPN + IPsec + Firewall)...")
            run_lab_simulation(
                start_firewall=True,
                start_openvpn=True,
                start_ipsec=True,
                simulate_traffic=True,
                show_logs=True
            )
        elif choice == "5":
            print("\n🔥 Regras de firewall atuais:")
            fw = FirewallSim()
            fw.print_rules()
        elif choice == "6":
            print("\n📜 Logs completos do laboratório:")
            run_lab_simulation(
                start_firewall=True,
                start_openvpn=True,
                start_ipsec=True,
                simulate_traffic=False,
                show_logs=True
            )
        elif choice == "0":
            print("Saindo do laboratório...")
            sys.exit(0)
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main_menu()
