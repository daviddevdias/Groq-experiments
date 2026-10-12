import os 
from langchain_groq import ChatGroq


if not os.environ.get("GROQ_API_KEY"):
    raise SystemExit("Configure GROQ_API_KEY antes de executar.")

chat = ChatGroq(model="llama-3.3-70b-versatile")


nome = input('Seu nome é ')


print(f"Olá {nome}! Digite 'sair' para encerrar.")


historico = []

historico
