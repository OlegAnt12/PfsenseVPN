# PfsenseVPN
# pfsense-vpn-lab

Laboratório automático para pfSense com OpenVPN (remote-access) e IPsec (site-to-site).
Inclui: Terraform (opcional), Ansible, scripts de cliente, testes automatizados e CI.

## Estrutura
Veja a árvore de ficheiros no repositório (descrita no enunciado do projeto).

## Requisitos
- pfSense CE/Plus (versão testada: documentar aqui)
- Ansible >= 2.9
- Terraform (opcional)
- openvpn, wireguard-tools (opcional)
- curl, jq, tcpdump, nc, ping, traceroute
- Acesso SSH e WebConfigurator/API ao pfSense

## Como usar (exemplo rápido)
1. Provisionar VMs: `terraform/` ou criar VMs manualmente.
2. Editar `ansible/inventories/hosts.yml` com IPs e credenciais do pfSense.
3. Executar playbooks:
   - `ansible-playbook -i ansible/inventories/hosts.yml ansible/playbooks/openvpn-server.yml`
   - `ansible-playbook -i ansible/inventories/hosts.yml ansible/playbooks/ipsec-site-to-site.yml`
4. Gerar/baixar perfis `.ovpn` em `examples/` e testar com `scripts/client_connect_ovpn.sh`.
5. Executar testes: `./tests/test_openvpn_connect.sh`

## Testes automatizados
Scripts em `tests/` geram `tests/artifacts/` com logs e capturas (tcpdump). CI (GitHub Actions) executa testes quando configurado para apontar para um lab.

## Critérios de aceitação
(ver enunciado — Conexão, Roteamento, Firewall, Logs, Idempotência)

