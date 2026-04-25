# ROUGHEN v1.0 - Painel de Análise Free Fire

**Versão 1.0 - Roughen**

## 🎯 Sobre

ROUGHEN é um painel avançado para Termux que analisa dispositivos Android em busca de anomalias em Free Fire (Normal e Max). Detecta root, arquivos suspeitos, Shizuku em execução e depuração ativa.

## 🚀 Instalação One-Line

Copie e cole no Termux:

```bash
pkg install git python3 android-tools -y && rm -rf ROUGHEN && git clone https://github.com/trashmercuryr/ROUGHEN && cd ROUGHEN && python3 roughen.py
```

## ✨ Funcionalidades

✅ **Conexão WiFi ADB**
- Guia passo-a-passo de emparelhamento
- Porta de emparelhamento: 32867
- Porta fixa: 5555

✅ **Análise Free Fire Normal**
- Detecção de Root/Jailbreak
- Verificação de Shizuku
- Detecção de depuração
- Análise de arquivos suspeitos

✅ **Análise Free Fire Max**
- Mesmas verificações do FF Normal
- Suporte específico para FF Max

✅ **Informações do Dispositivo**
- Fabricante
- Modelo
- Versão Android
- Espaço de armazenamento
- IP do dispositivo

✅ **Alertas APLICAR W.O**
- Notificação visual de violações
- Lista detalhada de anomalias

## 📱 Menu Principal

```
[0] ➤ Conectar via ADB WiFi
[1] ➤ Analisar Free Fire Normal
[2] ➤ Analisar Free Fire Max
[3] ➤ Informações do Dispositivo
[9] ➤ Sair
```

## 🔧 Requisitos

- Termux instalado
- Android 6.0+
- Acesso à internet
- Python 3.7+

## 📝 Como Usar

### Passo 1: Preparar Android

1. Vá para **Configurações > Sobre o Telefone**
2. Toque 7 vezes em **"Número da compilação"**
3. Ative **"Opções de Desenvolvedor"**
4. Vá para **Configurações > Opções de Desenvolvedor**
5. Ative **"Depuração por WiFi"**

### Passo 2: Executar ROUGHEN

```bash
pkg install git python3 android-tools -y && rm -rf ROUGHEN && git clone https://github.com/trashmercuryr/ROUGHEN && cd ROUGHEN && python3 roughen.py
```

### Passo 3: Conectar via WiFi

1. No painel, selecione **[0]**
2. Digite o código de emparelhamento (6 dígitos)
3. Digite o IP do seu dispositivo
4. Conexão feita!

### Passo 4: Analisar Free Fire

1. Escolha **[1]** para FF Normal ou **[2]** para FF Max
2. Aguarde a análise
3. Veja o relatório com todas as verificações

## 🎨 Interface

- Cores vibrantes e formatação profissional
- Menu interativo e fácil de usar
- Interface estilo Keller
- Alertas visuais claros

## 🔍 O que é Verificado

### Root/Jailbreak
- Binários de root em locais conhecidos
- Verificação de Magisk
- Detecção de SuperSU

### Shizuku
- Verifica se o serviço está em execução
- Detecta pacote moe.shizuku.server

### Depuração
- Status de depuração USB
- Status de depuração WiFi
- Verificação de ADB ativa

### Arquivos Suspeitos
- Mods de Free Fire
- Ferramentas de hack
- Softwares de modificação

## ⚙️ Configuração

Arquivos de configuração em `~/.roughen/config.json`

## 📖 Documentação Completa

Veja [QUICKSTART.md](QUICKSTART.md) para mais detalhes

## 🔐 Privacidade

- Todas as verificações ocorrem localmente
- Nenhum dado é enviado para servidores externos
- Código aberto para análise

## 📞 Suporte

Repositório: https://github.com/trashmercuryr/ROUGHEN

## 📄 Licença

MIT License

---

**ROUGHEN v1.0** 🔴 - Pronto para proteger!
