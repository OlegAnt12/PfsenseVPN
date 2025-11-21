# simulate_ipsec.py
import time
import random
from simulate_log import log_ipsec

class IPSecSim:
    """
    Simula túneis IPsec site-to-site entre pfSense.
    Gera logs de handshake, tempo de estabelecimento e possíveis falhas.
    """

    def __init__(self, peer_a="pf1", peer_b="pf2"):
        self.peer_a = peer_a
        self.peer_b = peer_b
        self.tunnel_established = False
        self.logs = []

    def establish_tunnel(self):
        """
        Simula estabelecimento de túnel IPsec.
        Pode incluir pequenas falhas aleatórias para teste de resiliência.
        """
        log_ipsec(f"Iniciando estabelecimento do túnel {self.peer_a} ↔ {self.peer_b}")
        start_time = time.time()
        time.sleep(0.3)  # Simula handshake

        # Simula falha aleatória de handshake (10% de chance)
        if random.random() < 0.1:
            self.tunnel_established = False
            log_ipsec(f"Falha no handshake IPsec entre {self.peer_a} ↔ {self.peer_b}")
            self.logs.append(f"{time.strftime('%Y-%m-%dT%H:%M:%S')} - Falha no handshake IPsec")
        else:
            self.tunnel_established = True
            elapsed = round(time.time() - start_time, 2)
            log_ipsec(f"IPsec SA established entre {self.peer_a} ↔ {self.peer_b} (tempo: {elapsed}s)")
            self.logs.append(f"{time.strftime('%Y-%m-%dT%H:%M:%S')} - IPsec SA established entre {self.peer_a} ↔ {self.peer_b} (tempo: {elapsed}s)")

    def disconnect_tunnel(self):
        """
        Simula desconexão do túnel IPsec.
        """
        if self.tunnel_established:
            log_ipsec(f"Túnel IPsec {self.peer_a} ↔ {self.peer_b} desconectado")
            self.logs.append(f"{time.strftime('%Y-%m-%dT%H:%M:%S')} - Túnel IPsec desconectado")
            self.tunnel_established = False

    def print_logs(self):
        """
        Imprime logs detalhados do túnel IPsec.
        """
        print("\n[ 📜 IPSEC LOGS ]")
        for entry in self.logs:
            print(entry)

        # Também imprime logs globais, caso existam
        try:
            global_logs = log_ipsec.__globals__["ipsec_logs"]
            for entry in global_logs:
                print(entry)
        except KeyError:
            pass
