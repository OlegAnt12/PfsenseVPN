# simulate_openvpn.py
import time
from simulate_log import log_openvpn

class OpenVPNSim:
    """
    Simulação de um servidor OpenVPN.
    Permite múltiplos clientes, sub-redes diferentes e logs detalhados.
    """

    def __init__(self, server_name="pf1", subnet="10.8.0.0/24"):
        self.server_name = server_name
        self.subnet = subnet
        self.clients = {}   # cliente -> IP atribuído
        self.logs = []

    def connect_client(self, client_name):
        """
        Simula a conexão de um cliente OpenVPN.
        Gera IP incremental a partir da subrede.
        """
        # Gerar IP baseado no número de clientes atuais
        ip_suffix = len(self.clients) + 2
        ip_parts = self.subnet.split(".")
        ip = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.{ip_suffix}"
        self.clients[client_name] = ip
        log_openvpn(f"Cliente {client_name} conectado → IP {ip}")
        self.logs.append(f"{time.strftime('%Y-%m-%dT%H:%M:%S')} - Cliente {client_name} conectado → IP {ip}")
        return ip

    def connect_multiple(self, client_list):
        """
        Conecta múltiplos clientes de uma vez.
        Retorna dicionário cliente -> IP.
        """
        for client in client_list:
            self.connect_client(client)
            time.sleep(0.1)  # Simulação de atraso de conexão
        return self.clients

    def disconnect_client(self, client_name):
        """
        Desconecta cliente da VPN.
        """
        if client_name in self.clients:
            ip = self.clients.pop(client_name)
            log_openvpn(f"Cliente {client_name} desconectado (IP {ip})")
            self.logs.append(f"{time.strftime('%Y-%m-%dT%H:%M:%S')} - Cliente {client_name} desconectado (IP {ip})")

    def print_logs(self):
        """
        Imprime logs detalhados da OpenVPN.
        """
        print("\n[ 📜 OPENVPN LOGS ]")
        for entry in self.logs:
            print(entry)

        # Também imprime logs globais, caso existam
        try:
            global_logs = log_openvpn.__globals__["openvpn_logs"]
            for entry in global_logs:
                print(entry)
        except KeyError:
            pass
