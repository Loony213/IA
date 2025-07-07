from app.repositories.openai_repository import OpenAIRepository

class ChatbotService:
    def __init__(self):
        self.openai_repo = OpenAIRepository()

    def get_chatbot_response(self, message: str) -> str:
        try:
            # Intentar obtener la respuesta del bot
            response = self.openai_repo.get_response(message)
            return response
        except Exception as e:
            # Captura cualquier error y proporciona más detalles
            raise Exception(f"Error al obtener la respuesta del bot: {str(e)}")
