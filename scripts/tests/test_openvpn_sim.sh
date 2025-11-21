#!/usr/bin/env bash
set -euo pipefail

echo "🚀 Teste de OpenVPN simulado"

python3 scripts/simulate_openvpn.py
python3 scripts/simulate_openvpn_client.py

# Verifica status dos clientes
for f in pf1/config/*_status.yml; do
    echo "Verificando $f"
    grep -q "connected: true" "$f" && echo "✓ $f OK" || echo "✗ $f falhou"
done
