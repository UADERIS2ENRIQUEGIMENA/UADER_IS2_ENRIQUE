import sys
import openai

# Definir el buffer para almacenar las consultas y respuestas
buffer_conversacion = []

# Definir la función para verificar el texto
def verificar_texto(consulta):
    return consulta.strip() != ""

# Función para interactuar con el modelo de OpenAI
def interactuar_chat_gpt(consulta):
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": "contexto"},
                {"role": "user", "content": "usertask"},
                {"role": "user", "content": consulta}
            ],
            temperature=1,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].message.content
    except openai.OpenAIError as e:
        print("Error en la invocación del modelo de chatGPT:", e)
        return None

def main():
    # Verificar si se proporcionó el argumento "--convers"
    if "--convers" not in sys.argv:
        print("El argumento '--convers' no fue proporcionado.")
        return

    try:
        while True:
            # Aceptación de consulta desde el usuario
            try:
                consulta = input("Ingrese su consulta: ")  # Solicitar la consulta al usuario
            except KeyboardInterrupt:
                print("\nSe ha interrumpido la entrada del usuario.")
                return

            # Tratamiento de la consulta
            try:
                if verificar_texto(consulta):
                    # Agregar la consulta al buffer de conversación
                    buffer_conversacion.append(consulta)

                    # Obtener la última consulta para la interacción con chatGPT
                    consulta_interaccion = buffer_conversacion[-1]

                    # Interactuar con chatGPT utilizando la última consulta
                    respuesta_chat_gpt = interactuar_chat_gpt(consulta_interaccion)

                    # Agregar la respuesta de chatGPT al buffer de conversación
                    if respuesta_chat_gpt:
                        buffer_conversacion.append(respuesta_chat_gpt)

                        # Imprimir la respuesta de chatGPT
                        print("chatGPT:", respuesta_chat_gpt)
                    else:
                        print("No se pudo obtener respuesta del modelo.")
                else:
                    print("La consulta está vacía.")
            except Exception as e:
                print("Error en el tratamiento de la consulta:", e)
    except Exception as e:
        print("Error general:", e)

