import streamlit as st

from src.utils import chat

st.set_page_config(page_title="Sample Chatbot Interface", page_icon="🤖", layout="wide")

st.title("🤖 Sample Chatbot Interface")

chatbot_options = [
    "Bob",
    "Sarah",
]

selected_chatbot = st.selectbox("Choose your chatbot:", chatbot_options, index=0)

st.write(f"Currently chatting with: **{selected_chatbot}**")

if "messages" not in st.session_state:
    st.session_state.messages = []

chat_container = st.container(height=400)

with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("What would you like to say?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with chat_container:
        with st.chat_message("user"):
            st.markdown(prompt)

    response = chat(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})

    with chat_container:
        with st.chat_message("assistant"):
            st.markdown(response)
