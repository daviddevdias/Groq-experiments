# Experimentos com Groq

Protótipo em Python que combina captura de voz, respostas de um modelo via Groq e síntese de áudio com ElevenLabs.

## Fluxo

1. O usuário informa o nome no terminal.
2. `SpeechRecognition` captura o microfone e transcreve a fala usando o serviço de reconhecimento do Google.
3. `ChatGroq` envia a pergunta e parte do histórico para o modelo configurado.
4. ElevenLabs gera áudio da resposta e `pygame` reproduz o arquivo.
5. Comandos que contêm “sair”, “encerrar” ou “fechar” encerram o programa.

## Requisitos

Python 3.11, microfone, saída de áudio, internet e credenciais próprias de Groq e ElevenLabs. O acesso aos serviços depende da disponibilidade e dos limites da sua conta.

## 📦 Instalação

```bash
git clone https://github.com/daviddevdias/Groq-experiments.git
cd Groq-experiments
python -m venv .venv
```

### Windows com PowerShell

Ative o ambiente:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Linux e macOS

```bash
source .venv/bin/activate
```

### Dependências

Instale os pacotes no ambiente ativado:

```bash
python -m pip install -r requirements.txt
```

`PyAudio` pode exigir dependências de áudio do sistema. A lista de pacotes ainda não representa um ambiente validado de ponta a ponta.

## 🚀 Configuração e execução

### Windows com PowerShell

Configure as chaves na sessão atual:

```powershell
$env:GROQ_API_KEY = "sua-chave-groq"
$env:ELEVENLABS_API_KEY = "sua-chave-elevenlabs"
python Groq.py
```

### Linux e macOS

```bash
export GROQ_API_KEY="sua-chave-groq"
export ELEVENLABS_API_KEY="sua-chave-elevenlabs"
python Groq.py
```

`.env.example` documenta as variáveis. O programa **não carrega arquivos .env automaticamente**. O dispositivo de áudio, a voz e o modelo estão configurados em `Groq.py` e podem precisar de ajuste.

## 🔒 Segurança e dados

Nunca publique chaves de API. Credenciais expostas anteriormente devem ser revogadas nos provedores: removê-las do código atual não as remove do histórico do Git.

A fala é enviada ao serviço de reconhecimento, as perguntas e o histórico são enviados ao Groq e o texto da resposta ao ElevenLabs. O áudio gerado é gravado em `audios/fala.mp3`. O nome digitado serve para personalizar a conversa; não é autenticação.

## Arquivos e limites

- `Groq.py`: protótipo principal com voz.
- `V1.py`: exemplo de conversa no terminal com resposta fixa.
- `V1_copy.py`: rascunho de inicialização do cliente, sem loop de conversa completo.
- `Zone.py` e `Primeiro passos/`: material experimental.

O histórico atual armazena apenas as perguntas do usuário e permanece em memória. Não há testes completos de microfone ou APIs externas. A pasta `venv` está versionada; o `.gitignore` evita novas inclusões, mas não remove o conteúdo já rastreado.

## Próximos passos

Remover o ambiente virtual do controle de versão, fixar dependências após validação, tratar falhas de rede e permitir seleção do dispositivo de áudio.
