# mini_bot_uach_vertical.py
import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="Mini Chatbot FCA-UACH",
    page_icon="💬",
    layout="wide"
)

# 2. Perfil en la barra lateral
st.sidebar.header("Perfil")
st.sidebar.image("https://via.placeholder.com/120", width=120)
st.sidebar.markdown(
    "**Dr. José Francisco Aldrete Enríquez**\n\n"
    "Profesor Investigador\n\n"
    "Facultad de Contaduría y Administración\n\n"
    "Universidad Autónoma de Chihuahua"
)

# 3. Título y bienvenida
st.title("💬 Mini Chatbot FCA-UACH")
st.markdown(
    "Bienvenido al mini chatbot. "
    "Este asistente repetirá textualmente lo que usted escriba, "
    "ahora sus respuestas se mostrarán en vertical."
)

# 4. Inicializar historial
if "historial" not in st.session_state:
    st.session_state.historial = []

# 5. Entrada de usuario
entrada = st.chat_input("Escriba su mensaje aquí…")
if entrada:
    st.session_state.historial.append({"role": "user", "text": entrada})
    respuesta = f"{entrada}  ← eso dijiste"
    st.session_state.historial.append({"role": "assistant", "text": respuesta})

# 6. Botón de reinicio en el cuerpo principal
if st.button("🔄 Reiniciar chat"):
    st.session_state.historial.clear()

# 7. Mostrar todo el historial (respuestas en vertical)
for mensaje in st.session_state.historial:
    if mensaje["role"] == "user":
        st.markdown(f"**Usted:** {mensaje['text']}")
    else:
        # CSS para orientación vertical
        st.markdown(
            f"<div style='writing-mode: vertical-lr; white-space: nowrap; "
            f"border-left: 1px solid #ddd; padding-left: 8px; margin: 8px 0;'>"
            f"{mensaje['text']}</div>",
            unsafe_allow_html=True
        )

