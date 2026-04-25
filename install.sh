#!/bin/bash

# ROUGHEN v1.0 - Instalador One-Line
# Comando: pkg install git python3 android-tools -y && rm -rf ROUGHEN && git clone https://github.com/trashmercuryr/ROUGHEN && cd ROUGHEN && python3 roughen.py

set -e

# Cores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m'

# Banner
clear
echo -e "${CYAN}"
echo "╔════════════════════════════════════════╗"
echo "║  ${MAGENTA}ROUGHEN v1.0 - Painel Avançado${CYAN}     ║"
echo "║  ${MAGENTA}Free Fire Analyzer${CYAN}                ║"
echo "╚════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

echo -e "${BLUE}[*]${NC} Atualizando repositórios..."
apt update -y > /dev/null 2>&1

echo -e "${BLUE}[*]${NC} Instalando dependências..."
apt install -y git python3 android-tools > /dev/null 2>&1

echo -e "${GREEN}[✓]${NC} Dependências instaladas!"
echo ""

echo -e "${BLUE}[*]${NC} Removendo versão anterior (se existir)..."
rm -rf ROUGHEN

echo -e "${BLUE}[*]${NC} Clonando ROUGHEN do repositório..."
git clone https://github.com/trashmercuryr/ROUGHEN

echo -e "${GREEN}[✓]${NC} Repositório clonado com sucesso!"
echo ""

cd ROUGHEN

echo -e "${BLUE}[*]${NC} Instalando dependências Python..."
pip install -q requests colorama 2>/dev/null || true

echo -e "${GREEN}[✓]${NC} Tudo pronto!"
echo ""

echo -e "${CYAN}╔════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║  Iniciando ROUGHEN v1.0...            ║${NC}"
echo -e "${CYAN}╚════════════════════════════════════════╝${NC}"
echo ""

# Executar o painel
python3 roughen.py
