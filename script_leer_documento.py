# Requisitos: pip install pypdf
from pypdf import PdfReader
import os

class LeerDocumento():

    def __init__(self):
        self.ruta_pdf = os.path.join(os.path.dirname(__file__), "documentos", "pdf_prueba.pdf")

    def leer_pdf(self):
        """
        Lee y extrae texto de un archivo PDF.

        Args:
            ruta_pdf (str): Ruta al archivo PDF.

        Returns:
            str: Texto extraído o mensaje de error.
        """
        if not os.path.isfile(self.ruta_pdf):
            return f"Error: No se encontró el archivo '{self.ruta_pdf}'."

        try:
            reader = PdfReader(self.ruta_pdf)
            texto_completo = ""

            for num_pagina, pagina in enumerate(reader.pages, start=1):
                texto = pagina.extract_text()
                if texto:
                    texto_completo += f"\n--- Página {num_pagina} ---\n{texto}\n"
                else:
                    texto_completo += f"\n--- Página {num_pagina} ---\n[Sin texto extraíble]\n"

            return texto_completo.strip()

        except Exception as e:
            return f"Error al leer el PDF: {e}"

