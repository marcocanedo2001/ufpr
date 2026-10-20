# Guia Geral: Deploy de App Streamlit em VM Oracle Cloud

Este guia mostra um caminho direto para publicar uma aplicação Streamlit em uma
instância Ubuntu da Oracle Cloud usando SSH, `venv`, firewall interno e serviço
`systemd`.

## 1. Pré-requisitos

No computador local:

```bash
ssh <host-ssh>
rsync --version
```

No arquivo `~/.ssh/config`, tenha um host configurado para a VM:

```sshconfig
Host oracle-app
  HostName <ip-publico-da-vm>
  User ubuntu
  IdentityFile ~/.ssh/<sua-chave-privada>
  IdentitiesOnly yes
```

Teste:

```bash
ssh oracle-app
```

## 2. Liberar a Porta na OCI

No Console da Oracle:

1. Abra a instância.
2. Vá em **Rede**.
3. Clique na **sub-rede** da VNIC principal.
4. Abra a **Security List** associada.
5. Clique em **Adicionar Regras de Entrada**.

Regra para Streamlit:

```text
Tipo de origem: CIDR
CIDR de origem: <seu-ip-publico>/32
Protocolo IP: TCP
Intervalo de portas de origem: deixar em branco
Intervalo de portas de destino: 8501
Descrição: Streamlit app
```

Para descobrir seu IP público:

```bash
curl -4 https://ifconfig.me
```

## 3. Enviar a Aplicação

Na pasta local do projeto:

```bash
ssh oracle-app 'mkdir -p ~/app-streamlit'
rsync -av app.py requirements.txt README.md .env .env.example oracle-app:~/app-streamlit/
```

Evite enviar arquivos temporários, logs, `__pycache__`, notebooks pesados ou
chaves privadas.

Proteja o `.env` na VM:

```bash
ssh oracle-app 'chmod 600 ~/app-streamlit/.env'
```

## 4. Preparar Python e Dependências

Na VM:

```bash
ssh oracle-app 'sudo apt-get update && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y python3.12-venv'
```

Criar o ambiente virtual:

```bash
ssh oracle-app 'cd ~/app-streamlit && python3 -m venv .venv'
```

Instalar dependências:

```bash
ssh oracle-app 'cd ~/app-streamlit && .venv/bin/python -m pip install --upgrade pip && .venv/bin/python -m pip install -r requirements.txt'
```

## 5. Liberar a Porta no Firewall Interno da VM

Algumas imagens Ubuntu da Oracle rejeitam portas que não estejam explicitamente
liberadas no `iptables`.

Libere a porta `8501`:

```bash
ssh oracle-app 'sudo iptables -C INPUT -p tcp -m state --state NEW -m tcp --dport 8501 -j ACCEPT || sudo iptables -I INPUT 5 -p tcp -m state --state NEW -m tcp --dport 8501 -j ACCEPT'
```

Salvar a regra para sobreviver a reboot:

```bash
ssh oracle-app 'sudo netfilter-persistent save'
```

Confirmar:

```bash
ssh oracle-app 'sudo iptables -S INPUT | grep 8501'
```

## 6. Criar Serviço systemd

Crie o serviço:

```bash
ssh oracle-app 'sudo tee /etc/systemd/system/app-streamlit.service >/dev/null <<EOF
[Unit]
Description=Streamlit app
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/app-streamlit
Environment=PATH=/home/ubuntu/app-streamlit/.venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ExecStart=/home/ubuntu/app-streamlit/.venv/bin/streamlit run /home/ubuntu/app-streamlit/app.py --server.address=0.0.0.0 --server.port=8501 --server.headless=true --browser.gatherUsageStats=false
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF'
```

Ative e inicie:

```bash
ssh oracle-app 'sudo systemctl daemon-reload && sudo systemctl enable --now app-streamlit.service'
```

## 7. Testar

Verificar serviço:

```bash
ssh oracle-app 'systemctl status app-streamlit.service --no-pager'
```

Verificar se a porta está aberta dentro da VM:

```bash
ssh oracle-app 'ss -ltnp | grep 8501'
```

Testar HTTP dentro da VM:

```bash
ssh oracle-app 'curl -I http://127.0.0.1:8501'
```

Testar do computador local:

```bash
nc -vz -w 5 <ip-publico-da-vm> 8501
```

Abrir no navegador:

```text
http://<ip-publico-da-vm>:8501
```

## 8. Comandos Úteis

Reiniciar a aplicação:

```bash
ssh oracle-app 'sudo systemctl restart app-streamlit.service'
```

Ver logs:

```bash
ssh oracle-app 'journalctl -u app-streamlit.service -n 100 --no-pager'
```

Parar a aplicação:

```bash
ssh oracle-app 'sudo systemctl stop app-streamlit.service'
```

## Observações de Segurança

- Não envie chave privada SSH para a VM.
- Não publique `.env` em GitHub.
- Prefira liberar a porta `8501` apenas para o seu IP com `/32`.
- Se seu IP público mudar, atualize a regra de entrada na OCI.
- Para produção real, considere usar HTTPS, domínio e proxy reverso como Nginx.
