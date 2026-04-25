#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ROUGHEN v1.0 - Painel de Análise Free Fire
Autor: trashmercuryr
Descrição: Painel avançado para análise de anomalias em Free Fire via ADB WiFi
"""

import os
import sys
import subprocess
import json
import time
from pathlib import Path
from datetime import datetime

try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
except ImportError:
    os.system('pip install -q colorama')
    from colorama import Fore, Back, Style, init
    init(autoreset=True)

# ============================================================================
# CORES E FORMATAÇÃO
# ============================================================================

class Colors:
    """Paleta de cores para o painel"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BLACK = '\033[90m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'

# ============================================================================
# CLASSE PRINCIPAL DO PAINEL
# ============================================================================

class ROUGHEN:
    """Painel principal de análise ROUGHEN"""
    
    def __init__(self):
        self.version = "1.0"
        self.device_connected = False
        self.device_info = {}
        self.suspicious_files = [
            '/system/xbin/su',
            '/system/bin/su',
            '/data/data/com.koushikdutta.superuser',
            '/data/data/eu.chainfire.supersu',
            '/data/data/com.topjohnwu.magisk',
            '/system/app/Superuser.apk',
            '/system/xbin/daemonsu',
        ]
        self.ff_packages = [
            'com.dts.freefireth',
            'com.dts.freefire',
        ]
        self.ff_max_packages = [
            'com.dts.freefiremax',
        ]
        self.shizuku_package = 'moe.shizuku.server'
    
    def clear_screen(self):
        """Limpa a tela do terminal"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def print_banner(self):
        """Exibe banner principal"""
        self.clear_screen()
        print(f"{Colors.CYAN}{Colors.BOLD}")
        print("╔════════════════════════════════════════╗")
        print("║  ROUGHEN v1.0 - Painel Avançado       ║")
        print("║  Free Fire Analyzer                    ║")
        print("║  By: trashmercuryr                     ║")
        print("╚════════════════════════════════════════╝")
        print(f"{Colors.RESET}")
    
    def print_menu(self):
        """Exibe menu principal"""
        print(f"\n{Colors.CYAN}{Colors.BOLD}┌─ MENU PRINCIPAL ─────────────────────┐{Colors.RESET}")
        print(f"│")
        print(f"│  {Colors.GREEN}[0]{Colors.RESET} ➤ Conectar via ADB WiFi")
        print(f"│     └─ Emparelhamento e Conexão")
        print(f"│")
        print(f"│  {Colors.YELLOW}[1]{Colors.RESET} ➤ Analisar Free Fire Normal")
        print(f"│")
        print(f"│  {Colors.YELLOW}[2]{Colors.RESET} ➤ Analisar Free Fire Max")
        print(f"│")
        print(f"│  {Colors.BLUE}[3]{Colors.RESET} ➤ Informações do Dispositivo")
        print(f"│")
        print(f"│  {Colors.RED}[9]{Colors.RESET} ➤ Sair")
        print(f"│")
        print(f"{Colors.CYAN}└────────────────────────────────────────┘{Colors.RESET}")
    
    def adb_wifi_connection(self):
        """Guia interativo para conexão via WiFi ADB"""
        self.clear_screen()
        print(f"{Colors.CYAN}{Colors.BOLD}")
        print("╔════════════════════════════════════════╗")
        print("║  Conexão via ADB WiFi - ROUGHEN       ║")
        print("╚════════════════════════════════════════╝")
        print(f"{Colors.RESET}\n")
        
        print(f"{Colors.GREEN}{Colors.BOLD}PASSO 1: Porta de Emparelhamento{Colors.RESET}")
        print(f"Use a porta: {Colors.YELLOW}{Colors.BOLD}32867{Colors.RESET}")
        print(f"Comando: {Colors.CYAN}adb pair 192.168.X.X:32867{Colors.RESET}\n")
        
        print(f"{Colors.GREEN}{Colors.BOLD}PASSO 2: Código de Emparelhamento{Colors.RESET}")
        pairing_code = input(f"{Colors.BLUE}Digite o código (6 dígitos): {Colors.RESET}")
        
        if len(pairing_code) != 6:
            print(f"{Colors.RED}Código inválido!{Colors.RESET}")
            return
        
        print(f"\n{Colors.GREEN}{Colors.BOLD}PASSO 3: IP do Dispositivo{Colors.RESET}")
        device_ip = input(f"{Colors.BLUE}Digite o IP: {Colors.RESET}")
        
        print(f"\n{Colors.YELLOW}{Colors.BOLD}Conectando... {Colors.RESET}")
        print(f"Comando: {Colors.CYAN}adb connect {device_ip}:5555{Colors.RESET}\n")
        
        # Tentar conexão
        result = os.system(f'adb connect {device_ip}:5555 > /dev/null 2>&1')
        
        if result == 0:
            print(f"{Colors.GREEN}{Colors.BOLD}✓ Conectado com sucesso!{Colors.RESET}\n")
            self.device_connected = True
            self.get_device_info()
        else:
            print(f"{Colors.RED}{Colors.BOLD}✗ Falha na conexão!{Colors.RESET}\n")
        
        input(f"{Colors.BLUE}Pressione ENTER para continuar...{Colors.RESET}")
    
    def adb_command(self, cmd):
        """Executa comando ADB"""
        try:
            result = subprocess.run(f'adb shell {cmd}', shell=True, capture_output=True, text=True, timeout=5)
            return result.stdout.strip()
        except:
            return ""
    
    def get_device_info(self):
        """Obtém informações do dispositivo"""
        try:
            self.device_info['fabricante'] = self.adb_command('getprop ro.product.manufacturer')
            self.device_info['modelo'] = self.adb_command('getprop ro.product.model')
            self.device_info['android'] = self.adb_command('getprop ro.build.version.release')
            self.device_info['ip'] = self.adb_command('getprop dhcp.wlan0.ipaddress')
            self.device_info['armazenamento'] = self.adb_command('df /data | tail -1 | awk \"{print $2}\"')
        except:
            pass
    
    def check_root(self):
        """Verifica se dispositivo tem root"""
        violations = []
        
        for path in self.suspicious_files:
            output = self.adb_command(f'test -f {path} && echo "existe" || echo "nao existe"')
            if 'existe' in output:
                violations.append(f"Arquivo de Root encontrado: {path}")
        
        return violations
    
    def check_shizuku(self):
        """Verifica se Shizuku está em execução"""
        output = self.adb_command(f'pm list packages | grep {self.shizuku_package}')
        if self.shizuku_package in output:
            return [f"Shizuku detectado: {self.shizuku_package}"]
        return []
    
    def check_debug(self):
        """Verifica status de depuração"""
        violations = []
        
        usb_debug = self.adb_command('getprop persist.sys.usb.config')
        if 'adb' in usb_debug:
            violations.append("Depuração USB ativa")
        
        # Verificar depuração WiFi
        output = self.adb_command('getprop service.adb.tcp.port')
        if output and output != '-1':
            violations.append("Depuração WiFi ativa")
        
        return violations
    
    def check_ff_files(self, ff_type='normal'):
        """Verifica arquivos suspeitos de Free Fire"""
        violations = []
        
        if ff_type == 'normal':
            packages = self.ff_packages
        else:
            packages = self.ff_max_packages
        
        for package in packages:
            # Verificar se pacote existe
            output = self.adb_command(f'pm list packages | grep {package}')
            if package in output:
                # Verificar arquivos suspeitos na pasta do jogo
                data_path = f'/data/data/{package}'
                suspicious = self.adb_command(f'find {data_path} -name "*.so" -o -name "*.apk" 2>/dev/null | wc -l')
                if suspicious and int(suspicious) > 50:
                    violations.append(f"Muitos arquivos suspeitos em {package}")
        
        return violations
    
    def analyze_ff(self, ff_type='normal'):
        """Análise completa de Free Fire"""
        self.clear_screen()
        
        type_name = "Free Fire Normal" if ff_type == 'normal' else "Free Fire Max"
        print(f"{Colors.CYAN}{Colors.BOLD}")
        print(f"╔════════════════════════════════════════╗")
        print(f"║  Analisando: {type_name:<28}║")
        print(f"╚════════════════════════════════════════╝")
        print(f"{Colors.RESET}\n")
        
        all_violations = []
        
        print(f"{Colors.BLUE}[*]{Colors.RESET} Verificando Root...")
        all_violations.extend(self.check_root())
        
        print(f"{Colors.BLUE}[*]{Colors.RESET} Verificando Shizuku...")
        all_violations.extend(self.check_shizuku())
        
        print(f"{Colors.BLUE}[*]{Colors.RESET} Verificando Depuração...")
        all_violations.extend(self.check_debug())
        
        print(f"{Colors.BLUE}[*]{Colors.RESET} Verificando arquivos de FF...")
        all_violations.extend(self.check_ff_files(ff_type))
        
        print(f"\n{Colors.CYAN}{Colors.BOLD}")
        print("╔════════════════════════════════════════╗")
        print("║  RESULTADO DA ANÁLISE                 ║")
        print("╚════════════════════════════════════════╝")
        print(f"{Colors.RESET}\n")
        
        if all_violations:
            print(f"{Colors.RED}{Colors.BOLD}⚠ APLICAR W.O - VIOLAÇÕES DETECTADAS!{Colors.RESET}\n")
            for i, violation in enumerate(all_violations, 1):
                print(f"{Colors.RED}[{i}]{Colors.RESET} {violation}")
        else:
            print(f"{Colors.GREEN}{Colors.BOLD}✓ Nenhuma violação detectada!{Colors.RESET}\n")
        
        self.print_device_info()
        
        input(f"\n{Colors.BLUE}Pressione ENTER para continuar...{Colors.RESET}")
    
    def print_device_info(self):
        """Exibe informações do dispositivo"""
        print(f"\n{Colors.CYAN}{Colors.BOLD}Informações do Dispositivo:{Colors.RESET}")
        print(f"├─ Fabricante: {self.device_info.get('fabricante', 'Desconhecido')}")
        print(f"├─ Modelo: {self.device_info.get('modelo', 'Desconhecido')}")
        print(f"├─ Android: {self.device_info.get('android', 'Desconhecido')}")
        print(f"├─ IP: {self.device_info.get('ip', 'Desconhecido')}")
        print(f"└─ Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    
    def show_device_info(self):
        """Mostra informações do dispositivo"""
        self.clear_screen()
        print(f"{Colors.CYAN}{Colors.BOLD}")
        print("╔════════════════════════════════════════╗")
        print("║  Informações do Dispositivo            ║")
        print("╚════════════════════════════════════════╝")
        print(f"{Colors.RESET}\n")
        
        self.print_device_info()
        
        input(f"\n{Colors.BLUE}Pressione ENTER para continuar...{Colors.RESET}")
    
    def run(self):
        """Loop principal do painel"""
        while True:
            self.print_banner()
            self.print_menu()
            
            choice = input(f"\n{Colors.BLUE}{Colors.BOLD}Digite sua opção: {Colors.RESET}")
            
            if choice == '0':
                self.adb_wifi_connection()
            elif choice == '1':
                if self.device_connected:
                    self.analyze_ff('normal')
                else:
                    print(f"{Colors.RED}Dispositivo não conectado! Use [0] primeiro.{Colors.RESET}")
                    input(f"{Colors.BLUE}Pressione ENTER...{Colors.RESET}")
            elif choice == '2':
                if self.device_connected:
                    self.analyze_ff('max')
                else:
                    print(f"{Colors.RED}Dispositivo não conectado! Use [0] primeiro.{Colors.RESET}")
                    input(f"{Colors.BLUE}Pressione ENTER...{Colors.RESET}")
            elif choice == '3':
                self.show_device_info()
            elif choice == '9':
                print(f"\n{Colors.GREEN}Obrigado por usar ROUGHEN v1.0!{Colors.RESET}\n")
                sys.exit(0)
            else:
                print(f"{Colors.RED}Opção inválida!{Colors.RESET}")
                input(f"{Colors.BLUE}Pressione ENTER...{Colors.RESET}")

# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    try:
        app = ROUGHEN()
        app.run()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Programa interrompido pelo usuário.{Colors.RESET}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}Erro: {e}{Colors.RESET}\n")
        sys.exit(1)
