import streamlit as st

st.set_page_config(
    page_title="Alphacoders",
    page_icon="🚀",
    layout="centered",
)

st.title("Hola Mundo, soy Alphacoders")
st.write(
    """
    Bienvenido a **Alphacoders**.

    Creamos soluciones de software, automatización e inteligencia artificial.
    """
)

st.divider()

st.page_link(
    "privacidad.py",
    label="Ver Política de Privacidad",
    icon="🔒",
)
