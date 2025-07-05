from flask import Flask
from flask_restful import Api
from flask_cors import CORS  # Importa CORS
from app.controllers.chatbot_controller import ChatbotController

def create_app():
    app = Flask(__name__)
    
    # Habilitar CORS globalmente
    CORS(app)

    # Registrar los controladores
    api = Api(app)
    api.add_resource(ChatbotController, "/ask")

    return app
