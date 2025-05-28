# mini_bot_uach.py
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Mini Chatbot FCA-UACH",
    page_icon="💬",
    layout="wide"
)

# Perfil en la barra lateral
st.sidebar.header("Perfil")
# Reemplace la URL por la de su foto o logo institucional
st.sidebar.image("https://via.placeholder.com/120", width=120)
st.sidebar.markdown(
    "**Dr. José Francisco Aldrete Enríquez**\n\n"
    "Profesor Investigador\n\n"
    "Facultad de Contaduría y Administración\n\n"
    "Universidad Autónoma de Chihuahua"
)

# Título y bienvenida
st.title("💬 Mini Chatbot FCA-UACH")
st.markdown(
    "Bienvenido al mini chatbot. "
    "Este asistente repetirá textualmente lo que usted escriba."
)

# Inicializar historial en sesión
if "historial" not in st.session_state:
    st.session_state.historial = []

# Entrada de usuario
entrada = st.chat_input("Escriba su mensaje aquí…")
if entrada:
    # Guardar y mostrar mensaje del usuario
    st.session_state.historial.append({"role": "user", "text": entrada})
    # Generar respuesta
    respuesta = f"{entrada}  ← eso dijiste"
    st.session_state.historial.append({"role": "assistant", "text": respuesta})

# Renderizar todo el historial
for mensaje in st.session_state.historial:
    st.chat_message(mensaje["role"]).write(mensaje["text"])

# Botón para reiniciar la conversación
if st.sidebar.button("🔄 Reiniciar chat"):
    st.session_state.historial = []
    st.experimental_rerun()

