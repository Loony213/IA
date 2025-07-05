import openai
from app.utils.openai_client import get_openai_client

class OpenAIRepository:
    def __init__(self):
        self.client = get_openai_client()

    def get_response(self, message: str) -> str:
        try:
            # Log del mensaje enviado
            print(f"Enviando mensaje a OpenAI: {message}")
            
            # Usar openai.ChatCompletion.create para obtener la respuesta del bot
            response = self.client.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Usamos GPT-3.5 o GPT-4
                messages=[{"role": "user", "content": message}],
                max_tokens=150
            )

            # Log de la respuesta de OpenAI
            print("Respuesta de OpenAI:", response)
            
            return response['choices'][0]['message']['content'].strip()
        except Exception as e:
            # Capturar errores y proporcionar detalles adicionales
            print(f"Error en la llamada a OpenAI: {str(e)}")
            raise Exception(f"Error al obtener la respuesta de OpenAI: {str(e)}")
