import openai
from app.config.config import Config

def get_openai_client():
    openai.api_key = Config.OPENAI_API_KEY 
    return openai  
