from conexion_agente import ConectarConAgente


def iniciar_chat():
    agente = ConectarConAgente()

    print("Chat iniciado. Escribe 'salir' para terminar.\n")

    while True:
        pregunta = input("Pregunta: ").strip()

        if pregunta.lower() == "salir":
            print("Hasta luego.")
            break

        if not pregunta:
            print("Escribe una pregunta.\n")
            continue

        respuesta = agente.obtener_respuesta_modelo_agente(pregunta)
        print(f"Respuesta: {respuesta}\n")


if __name__ == "__main__":
    iniciar_chat()
