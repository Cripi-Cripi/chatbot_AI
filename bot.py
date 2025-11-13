import streamlit as st

st.set_page_config(page_title="Asistente IA", layout="centered")
st.title("🤖 Asistente IA 24/7")
st.markdown("**Prueba gratis – responde al instante**")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Escribe tu pregunta..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Respuesta simulada (para demo)
    with st.chat_message("assistant"):
        response = f"✅ Claro, aquí tienes la respuesta a: «{prompt}». En la versión real uso ChatGPT-4o y puedo conectar tus documentos, WhatsApp o web."
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

st.caption("Demo pública – versión real incluye tu base de datos, memoria y conexión 24/7")