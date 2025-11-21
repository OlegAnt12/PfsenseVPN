# PfsenseVPN
# pfsense-vpn-lab

Laboratório automático para pfSense com OpenVPN (remote-access) e IPsec (site-to-site).
Inclui: scripts de cliente, testes automatizados e CI.

## Estrutura
Veja a árvore de ficheiros no repositório (descrita no enunciado do projeto).

## Requisitos
- pfSense CE/Plus (versão testada: documentar aqui)
- openvpn, wireguard-tools (opcional)

Gerar/baixar perfis `.ovpn` em `examples/` e testar com `scripts/client_connect_ovpn.sh`.
Executar testes: `./tests/test_openvpn_connect.sh`

## Testes automatizados
Scripts em `tests/` geram `tests/artifacts/` com logs e capturas (tcpdump). CI (GitHub Actions) executa testes quando configurado para apontar para um lab.

## Critérios de aceitação
(ver enunciado — Conexão, Roteamento, Firewall, Logs, Idempotência)

Objetivo do Projeto

O projeto é um laboratório de simulação de redes que permite testar cenários de pfSense com VPNs e políticas de firewall, sem necessidade de instalar pfSense real. Ele é 100% baseado em scripts Python, rodando localmente ou em Codespaces/GitHub, com logs detalhados e testes automatizados.

Funcionalidades principais

Simulação de pfSense

Dois dispositivos virtuais (pf1 e pf2) são simulados como firewalls/roteadores.

Cada pfSense mantém configurações de interfaces, rotas, VPNs e logs.

OpenVPN Remote Access (cliente/servidor)

Servidor OpenVPN simulado em pf1.

Suporte a múltiplos clientes conectando-se simultaneamente.

Geração de IPs virtuais para clientes e sub-redes configuráveis.

Registro de logs detalhados de conexão (cliente conectado, desconectado).

IPsec Site-to-Site

Túnel IPsec simulado entre pf1 e pf2.

Registro do tempo de handshake, estabelecimento de SA e falhas de conexão.

Suporte a múltiplas sub-redes interligadas via IPsec.

Firewall Simulado

Regras definidas por origem, destino, protocolo, porta e descrição.

Avaliação de pacotes simulados (ALLOW/DENY) entre clientes, LANs e sub-redes.

Logs detalhados de cada pacote, incluindo timestamp, regra aplicada e decisão.

Suporte a políticas entre sub-redes diferentes (ex.: OpenVPN ↔ LAN, LAN ↔ LAN via IPsec).

Simulação de Tráfego

Função simulate_traffic() envia pacotes simulados entre clientes, LANs e túneis VPN.

Verifica políticas de firewall, conectividade e acesso entre hosts/sub-redes.

Registra logs detalhados de cada evento.

Logs separados e detalhados

Firewall, OpenVPN e IPsec possuem logs separados, com timestamps e informações completas.

Permite debug e análise de tráfego simulado, como se fosse um laboratório real.

Automatização e testes

Scripts idempotentes: rodar várias vezes mantém o estado correto.

Suporte a execução em CI/CD, permitindo testes automatizados de conectividade, firewall e VPNs.

Objetivo educacional / prático

Estudo e prática de VPNs e firewalls sem necessidade de infraestrutura real.

Treino de troubleshooting e políticas de segurança em rede.

Visualização do comportamento de múltiplos clientes, sub-redes e túneis VPN.

Pode ser usado em disciplinas de redes, cibersegurança ou laboratórios virtuais.

Se você quiser, posso fazer um diagrama resumido do laboratório, mostrando pf1, pf2, OpenVPN, IPsec e sub-redes conectadas, para ficar visual e fácil de entender.

Quer que eu faça isso?
