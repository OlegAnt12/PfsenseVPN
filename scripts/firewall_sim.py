import time
import ipaddress

class FirewallSim:
    def __init__(self, device="pf1"):
        self.device = device
        self.rules = []
        self.logs = []

    def add_rule(self, action, src, dst, port="any", proto="any", description=""):
        """
        Adiciona uma regra de firewall
        action: 'ALLOW' ou 'DENY'
        src/dst: IP ou CIDR
        port: número ou 'any'
        proto: 'tcp', 'udp' ou 'any'
        description: texto explicativo
        """
        rule = {
            "action": action.upper(),
            "src": src,
            "dst": dst,
            "port": port,
            "proto": proto,
            "description": description
        }
        self.rules.append(rule)

    def print_rules(self):
        print("\n[ 🔥 FIREWALL RULES ]")
        for idx, r in enumerate(self.rules, 1):
            print(f"{idx}. {r['action']} {r['proto']} {r['src']} → {r['dst']}:{r['port']} ({r['description']})")

    def evaluate_packet(self, packet):
        """
        Avalia um pacote e retorna 'ALLOW' ou 'DENY'
        packet: dict {src, dst, port, proto}
        """
        for rule in self.rules:
            if self._match(packet, rule):
                self._log(packet, rule, rule["action"])
                return rule["action"]
        # Default deny
        self._log(packet, {"action": "default"}, "DENY")
        return "DENY"

    def _match(self, packet, rule):
        # Comparar IP/CIDR
        src_match = self._ip_in_subnet(packet["src"], rule["src"])
        dst_match = self._ip_in_subnet(packet["dst"], rule["dst"])
        port_match = (rule["port"] == "any") or (packet["port"] == rule["port"])
        proto_match = (rule["proto"] == "any") or (packet["proto"] == rule["proto"])
        return src_match and dst_match and port_match and proto_match

    def _ip_in_subnet(self, ip, subnet):
        try:
            return ipaddress.ip_address(ip) in ipaddress.ip_network(subnet, strict=False)
        except ValueError:
            return False

    def _log(self, packet, rule, decision):
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
        self.logs.append({
            "timestamp": timestamp,
            "packet": packet,
            "rule": rule,
            "decision": decision
        })

    def simulate_traffic(self, packets):
        """
        Avalia uma lista de pacotes simulados
        Retorna lista de tuples: (packet, decision)
        """
        results = []
        for pkt in packets:
            decision = self.evaluate_packet(pkt)
            results.append((pkt, decision))
        return results

    def print_logs(self):
        print("\n[ 📜 FIREWALL LOGS ]")
        for entry in self.logs:
            print(f"{entry['timestamp']} - {entry['decision']} - rule={entry['rule']} packet={entry['packet']}")


# Exemplo de uso
if __name__ == "__main__":
    fw = FirewallSim()
    fw.add_rule("ALLOW", "10.8.0.0/24", "192.168.1.0/24", "any", "any", "OpenVPN LAN access")
    fw.add_rule("DENY", "any", "192.168.1.0/24", 3389, "tcp", "Bloquear RDP")
    fw.print_rules()

    # Simular tráfego
    packets = [
        {"src": "10.8.0.2", "dst": "192.168.1.10", "port": 22, "proto": "tcp"},
        {"src": "10.8.0.3", "dst": "192.168.1.50", "port": 3389, "proto": "tcp"},
        {"src": "172.16.0.10", "dst": "192.168.1.5", "port": 22, "proto": "tcp"}
    ]
    results = fw.simulate_traffic(packets)
    fw.print_logs()
