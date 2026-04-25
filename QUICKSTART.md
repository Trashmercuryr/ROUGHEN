# ROUGHEN v1.0 - Guia de Início Rápido

## 🚀 Comando One-Line (Copie e Cole)

```bash
pkg install git python3 android-tools -y && rm -rf ROUGHEN && git clone https://github.com/trashmercuryr/ROUGHEN && cd ROUGHEN && python3 roughen.py
```

---

## 📱 Preparar seu Dispositivo Android

### Passo 1: Ativar Opções de Desenvolvedor
1. Vá para **Configurações > Sobre o Telefone**
2. Toque 7 vezes em **"Número da compilação"**
3. Volte para **Configurações**
4. Agora você verá **"Opções de Desenvolvedor"**
5. Entre em **"Opções de Desenvolvedor"**

### Passo 2: Ativar Depuração por WiFi
1. Em **Opções de Desenvolvedor**, procure por **"Depuração por WiFi"**
2. Ative a opção
3. Seu telefone mostrará:
   - **Porta de emparelhamento**: 32867
   - **Código de emparelhamento**: (6 dígitos)
   - **IP do dispositivo**: (exemplo: 192.168.1.100)

---

## 🎮 Usando ROUGHEN

### Primeira Execução

1. Abra **Termux**
2. Cole o comando one-line acima
3. Pressione **ENTER**
4. Aguarde a instalação (levará 2-3 minutos)

### Menu Principal

Quando ROUGHEN abrir, você verá:

```
[0] ➤ Conectar via ADB WiFi
[1] ➤ Analisar Free Fire Normal
[2] ➤ Analisar Free Fire Max
[3] ➤ Informações do Dispositivo
[9] ➤ Sair
```

### Conectar ao Dispositivo (Opção 0)

1. Digite **0** e pressione ENTER
2. ROUGHEN pedirá:
   - **Código de emparelhamento** (6 dígitos - copie do seu telefone)
   - **IP do dispositivo** (copie do seu telefone)
3. Aguarde a conexão

### Analisar Free Fire (Opção 1 ou 2)

1. Digite **1** para FF Normal ou **2** para FF Max
2. ROUGHEN analisará seu dispositivo
3. Se encontrar violações, exibirá **APLICAR W.O**
4. Veja o relatório completo

---

## 🔍 O que ROUGHEN Verifica

✅ **Root/Jailbreak**
- Detecta binários de root
- Verifica Magisk, SuperSU, etc

✅ **Shizuku**
- Verifica se está instalado
- Detecta se está em execução

✅ **Depuração**
- Status de depuração USB
- Status de depuração WiFi
- Verificação de ADB ativa

✅ **Arquivos Suspeitos**
- Mods de Free Fire
- Ferramentas de modificação
- Softwares de hack

---

## ⚡ Atalhos Rápidos

Após primeira instalação:

```bash
# Executar ROUGHEN novamente
cd ROUGHEN && python3 roughen.py

# Ou criar um atalho (alias)
alias roughen='cd ~/ROUGHEN && python3 roughen.py'

# Então basta digitar:
roughen
```

---

## 🆘 Solução de Problemas

### "Dispositivo não conectado"
- Certifique-se de que Depuração por WiFi está ativa
- Verifique se tem o código de emparelhamento correto
- Tente reconectar

### "ADB não encontrado"
- ROUGHEN instala automaticamente
- Se falhar, instale manualmente: `pkg install android-tools -y`

### "Erro de permissão"
- Pode ser necessário reiniciar o Termux
- Verifique permissões de armazenamento

---

## 📊 Interpretando Resultados

### ✓ Nenhuma Violação
Deveiço está limpo e seguro para jogar

### ⚠ APLICAR W.O
Seu dispositivo tem anomalias detectadas:
- Root ativado
- Shizuku em execução
- Depuração ativa
- Arquivos suspeitos encontrados

---

## 📞 Informações de Contato

**Repositório:** https://github.com/trashmercuryr/ROUGHEN

**Versão:** 1.0 - Roughen

**Autor:** trashmercuryr

---

**Aproveite ROUGHEN v1.0!** 🔴
