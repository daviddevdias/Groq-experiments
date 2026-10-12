# Experimentos com Groq

Protótipo de assistente que recebe perguntas por voz e reproduz respostas geradas por inteligência artificial.

## 📌 Funcionalidades

- Captura de áudio pelo microfone.
- Reconhecimento de fala em português.
- Respostas com Groq.
- Síntese de voz com ElevenLabs.

## Tecnologias

Python 3.11, SpeechRecognition, langchain-groq, ElevenLabs, pygame e PyAudio.

## 🚀 Como executar

```bash
git clone https://github.com/daviddevdias/Groq-experiments.git
cd Groq-experiments
python -m venv .venv
```

No PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
$env:GROQ_API_KEY = "sua-chave-groq"
$env:ELEVENLABS_API_KEY = "sua-chave-elevenlabs"
python Groq.py
```

Requer microfone, saída de áudio, internet e contas nos serviços utilizados. Diga “sair” ou “encerrar” para finalizar.

As variáveis são lidas do ambiente; arquivos .env não são carregados automaticamente. A fala é transcrita pelo serviço do Google, a pergunta é enviada ao Groq e a resposta ao ElevenLabs para gerar áudio. O modelo e o dispositivo de áudio podem ser ajustados em `Groq.py`.
