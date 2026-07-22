from script_leer_documento import LeerDocumento
import requests
import json
import os
from dotenv import load_dotenv

class ConectarConAgente():
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.session = requests.Session()
        self.session.trust_env = False
    
    def obtener_respuesta_modelo_agente(self, pregunta):
        if not self.api_key:
            return "Error: No se encontro la variable OPENROUTER_API_KEY en el archivo .env."

        lector_documento = LeerDocumento()
        lectura_archivo = lector_documento.leer_pdf()
            
        response = self.session.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "model": "openrouter/free",
                "messages": [
                {
                    "role": "system",
                    "content": self._obtener_promt(lectura_archivo, pregunta)
                }
                ]
            }),
            timeout=60,
            )
        
        if response.status_code == 200:
            data = response.json()
            respuesta = data['choices'][0]['message']['content']
        else:
            respuesta = f" {response.text} {response.status_code}"

        
        return respuesta
    
    def _obtener_promt(self, lectura_archivo, pregunta):
        prompt = f"""
            Eres un asistente que responde únicamente con base en el siguiente contenido.

            Contenido:
            {lectura_archivo}

            Pregunta del usuario:
            {pregunta}

            Instrucciones:
            - Responde únicamente utilizando la información del contenido proporcionado.
            - Si la respuesta no se encuentra en el contenido, responde: "No es posible responder esa pregunta con la información proporcionada."
            - Si el usuario solo saluda (por ejemplo: "Hola", "Buenos días", "¿Cómo estás?"), responde de manera amable y cordial.
            - No inventes información ni hagas suposiciones.
            - Evita responder basado en tu estructura interna.
            """
        return prompt
