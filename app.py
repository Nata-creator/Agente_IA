import streamlit as st
from requests.exceptions import RequestException

from conexion_agente import ConectarConAgente


st.set_page_config(
    page_title="Agente IA",
    layout="centered",
)


def obtener_agente():
    return ConectarConAgente()


st.title("Agente IA")
st.write("Escribe una pregunta sobre el documento PDF y el agente respondera.")

with st.form("formulario_pregunta"):
    pregunta = st.text_area(
        "Pregunta",
        placeholder="Ej: De que trata el documento?",
        height=120,
    )
    enviar = st.form_submit_button("Enviar pregunta")

if enviar:
    pregunta = pregunta.strip()

    if not pregunta:
        st.warning("Escribe una pregunta antes de enviar.")
    else:
        with st.spinner("Consultando el documento..."):
            try:
                respuesta = obtener_agente().obtener_respuesta_modelo_agente(pregunta)
            except RequestException as error:
                respuesta = f"No se pudo conectar con OpenRouter. Detalle: {error}"
            except Exception as error:
                respuesta = f"Ocurrio un error al consultar el agente: {error}"

        st.subheader("Respuesta")
        st.write(respuesta)
