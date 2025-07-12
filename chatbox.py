import streamlit as st

st.set_page_config(page_title="Chatbox - Rekayasa Perangkat Lunak", layout="centered")

st.title("Chatbox - Rekayasa Perangkat Lunak")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def respond(user_message):
    return "Halo, ini chatbox jurusan Rekayasa Perangkat Lunak!"

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Ketik pesan Anda di sini...", "")
    submitted = st.form_submit_button("Kirim")
    if submitted and user_input.strip():
        st.session_state.chat_history.append(("Anda", user_input.strip()))
        bot_reply = respond(user_input.strip())
        st.session_state.chat_history.append(("Bot", bot_reply))

chat_box = ""
for sender, message in st.session_state.chat_history:
    chat_box += f"**{sender}:** {message}\n\n"

st.markdown(chat_box)