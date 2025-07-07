from flask_restful import Resource
from flask import request, jsonify
from app.services.chatbot_service import ChatbotService

class ChatbotController(Resource):
    def __init__(self):
        self.chatbot_service = ChatbotService()

    def post(self):
        data = request.get_json()
        message = data.get("message")
        
        if not message:
            return {"error": "El mensaje es obligatorio"}, 400

        try:
            response = self.chatbot_service.get_chatbot_response(message)
            return jsonify({"botReply": response})
        except Exception as e:
            return {"error": str(e)}, 500
