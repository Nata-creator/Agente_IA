# Agente IA para consultar un PDF

Proyecto en Python que permite hacer preguntas sobre un documento PDF local. El agente lee el archivo 'documentos/pdf_prueba.pdf', envía el contenido junto con la pregunta a un modelo mediante OpenRouter y muestra la respuesta en consola.

## Características

- Lee el contenido de un PDF usando pypdf.
- Permite hacer preguntas desde la terminal.
- Responde usando únicamente la información del documento.
- Mantiene un flujo simple: preguntar, responder y volver a preguntar.
- Permite salir escribiendo 'salir'.

## Estructura del proyecto

Challenge-Agente-IA/
├── chat_pregunta.py          # Archivo principal para ejecutar el chat
├── conexion_agente.py        # Conexión con OpenRouter y generación del prompt
├── script_leer_documento.py  # Lectura del PDF
├── requirements.txt          # Dependencias del proyecto
└── documentos/
    └── pdf_prueba.pdf        # Documento consultado por el agente

## Requisitos

- Python instalado.
- Una API key de OpenRouter.
- El archivo PDF ubicado en:

documentos/pdf_prueba.pdf

## Instalación

1. Clona o descarga este repositorio.
git clone git@github.com:Nata-creator/Agente_IA.git

2. Crear entorno virtual para instalar dependencias
cmd
py -m venv .venv

3. Activar entorno virtual
cmd
.venv\Scripts\activate.bat

4. Instala las dependencias:
cmd
py -m pip install -r requirements.txt

5. Crea un archivo .env en la raíz del proyecto con tu API key:
OPENROUTER_API_KEY=tu_api_key_aqui

## Uso

Ejecuta el archivo principal:
py chat_pregunta.py

Luego escribe una pregunta:

Chat iniciado. Escribe 'salir' para terminar.

Pregunta: ¿De qué trata el documento?
Respuesta: ...

Pregunta: salir
Hasta luego.

## Interfaz sencilla con Streamlit

Tambien puedes ejecutar una interfaz web local para hacer preguntas al agente:

py -m streamlit run app.py

La pantalla permite:

- Escribir una pregunta sobre el PDF.
- Enviar la pregunta al agente.
- Mostrar la respuesta en pantalla.

Si aun no tienes Streamlit instalado, ejecuta primero:

py -m pip install -r requirements.txt

## Cómo funciona

1. chat_pregunta.py inicia el programa por consola.
2. El usuario escribe una pregunta.
3. conexion_agente.py carga la API key desde .env.
4. script_leer_documento.py extrae el texto del PDF.
5. Se envía el contenido del PDF y la pregunta al modelo.
6. La respuesta se imprime en la terminal.

## Notas

- Si el PDF no existe en la carpeta documentos, el programa devolverá un mensaje de error.
- Si la pregunta no se puede responder con el contenido del PDF, el agente debe indicarlo sin inventar información.
- Para cambiar el documento, reemplaza documentos/pdf_prueba.pdf por otro PDF con el mismo nombre o modifica la ruta en script_leer_documento.py.

## Evidencia
Link del agente en deploy https://agenteia-5etgtzvmac55s5xkj2vasd.streamlit.app/

## Ejemplo de pregunta
El documento es basado en el manejo del estres laboral
Pregunta: De que trata el documento
Posible respuesta del agente:
El documento es una guía práctica para manejar el estrés en el trabajo, que explica qué es el estrés laboral, sus señales comunes, causas, y ofrece estrategias efectivas (identificar causas, establecer límites, gestionar el tiempo, cuidar el bienestar físico y mental, buscar apoyo y fomentar un ambiente laboral positivo), además de incluir un plan de acción personal.

Pregunta: como puedo manejar el estrés
Posible respuesta del agente:
Basándote en la guía, puedes manejar el estrés laboral siguiendo estos pasos prácticos:

Identifica las causas principales – Piensa en lo que desencadena el estrés para ti (por ejemplo, sobrecarga de trabajo, falta de control, ambiente laboral difícil, inseguridad, falta de reconocimiento, o carga excesiva que afecta tu vida personal).

Establece límites claros –

Desconéctate del trabajo cuando termine la jornada.
Fiáate un horario fijo de inicio y fin y respétalo.
Aprende a decir "no" (con tacto) a nuevas tareas si estás sobrecargado, o negocia plazos más realistas.
Gestiona tu tiempo y tus tareas –

Prioriza usando la matriz de Eisenhower (urgente/importante).
Planifica las tareas al inicio del día o la noche anterior.
Evita la multitarea y co.............................
