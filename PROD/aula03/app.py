import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from chatlas import ChatOpenAICompletions

# =========================================================
# CONFIGURAÇÃO
# =========================================================

load_dotenv(dotenv_path=Path(__file__).with_name(".env"))

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

SYSTEM_PROMPT = """
Você é um assistente especializado em engenharia de prompt.

Seu papel é ajudar o usuário a explorar diferentes estratégias
de construção de prompts para modelos de linguagem.

Sempre que possível:
- explique conceitos de forma objetiva;
- mostre exemplos práticos;
- compare abordagens quando solicitado;
- mantenha respostas técnicas e concisas.
"""

# =========================================================
# STREAMLIT
# =========================================================

st.set_page_config(
    page_title="Engenharia de Prompt",
    page_icon="🤖",
    layout="wide"
)

if not NVIDIA_API_KEY:
    st.title("🤖 Engenharia de Prompt")
    st.error("A variável de ambiente NVIDIA_API_KEY não foi encontrada.")
    st.markdown("Crie um arquivo `.env` nesta pasta com:")
    st.code("NVIDIA_API_KEY=sua_chave_aqui", language="bash")
    st.stop()

chat = ChatOpenAICompletions(
    model="meta/llama-3.3-70b-instruct",
    api_key=NVIDIA_API_KEY,
    base_url="https://integrate.api.nvidia.com/v1"
)

st.title("🤖 Engenharia de Prompt")

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("Sobre")

    st.markdown("""
    Assistente especializado em Engenharia de Prompt.

    Faça perguntas sobre:
    - Prompt Engineering
    - LLMs
    - ChatGPT
    - Claude
    - Gemini
    - Agentes
    - RAG
    - Avaliação de prompts
    """)

    st.markdown("---")

    if st.button("Limpar conversa"):

        st.session_state.chat_history = [
            {
                "role": "assistant",
                "content": "Olá! Como posso ajudar você com Engenharia de Prompt?"
            }
        ]

        st.rerun()

# =========================================================
# HISTÓRICO
# =========================================================

if "chat_history" not in st.session_state:

    st.session_state.chat_history = [
        {
            "role": "assistant",
            "content": "Olá! Como posso ajudar você com Engenharia de Prompt?"
        }
    ]

# =========================================================
# EXIBE HISTÓRICO
# =========================================================

for message in st.session_state.chat_history:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# =========================================================
# INPUT
# =========================================================

user_question = st.chat_input(
    "Digite sua pergunta..."
)

# =========================================================
# PROCESSAMENTO
# =========================================================

if user_question:

    # Exibe usuário

    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    with st.chat_message("user"):

        st.markdown(user_question)

    # Monta contexto

    conversation = SYSTEM_PROMPT + "\n\n"

    for msg in st.session_state.chat_history:

        conversation += (
            f"{msg['role']}: "
            f"{msg['content']}\n"
        )

    # Gera resposta

    with st.chat_message("assistant"):

        with st.spinner("Pensando..."):

            response = chat.chat(
                conversation,
                stream=False
            )

            answer = str(response)

            st.markdown(answer)

    # Salva resposta

    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
