# mini_bot_uach_vertical_letras.py
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

# 3. Título y descripción
st.title("💬 Mini Chatbot FCA-UACH")
st.markdown(
    "Este asistente repetirá lo que usted escriba, "
    "mostrando cada **letra** de la respuesta en una línea distinta."
)

# 4. Inicializar historial en sesión
if "historial" not in st.session_state:
    st.session_state.historial = []

# 5. Entrada de usuario
entrada = st.chat_input("Escriba su mensaje aquí…")
if entrada:
    # Guardar mensaje del usuario
    st.session_state.historial.append({"role": "user", "text": entrada})
    # Generar y guardar respuesta
    respuesta = f"{entrada}  ← eso dijiste"
    st.session_state.historial.append({"role": "assistant", "text": respuesta})

# 6. Renderizar historial completo
for msg in st.session_state.historial:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["text"])
    else:
        # Construir un bloque HTML con <br> entre cada carácter
        html_vertical = "<br>".join(list(msg["text"]))
        st.chat_message("assistant").markdown(
            html_vertical,
            unsafe_allow_html=True
        )
