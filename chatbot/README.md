
# Chatbot Microservice 🤖

This microservice is part of the **IA** repository and provides the functionality to create a chatbot using OpenAI's GPT models. The service interacts with OpenAI's API to generate intelligent, context-aware responses, making it suitable for building AI-driven chat applications.

## Repository Link 📁
- [GitHub Repository](https://github.com/Loony213/IA)

## Docker Image 🐳
- **Docker Image:** `kamartinez/chatbot`

## Purpose 🎯
The **Chatbot Microservice** enables the creation of a chatbot powered by OpenAI's GPT models. It allows users to build and integrate intelligent chatbots that can engage in conversations, providing human-like responses based on the input received.

## Architecture Style 🏗️
- **Microservice Architecture:** This service is a standalone microservice that can be independently deployed and scaled.
- **Design Pattern:** The service follows the **MVC (Model-View-Controller)** design pattern to separate concerns, ensuring maintainability and scalability.

## Technologies 💻
- **Programming Language:** Python 3.x
- **Library:** OpenAI API for natural language processing
- **Containerization:** Docker (optional)

## Project Structure 🧑‍💻
The repository is structured as follows:

```
chatbot/
├── app/                      # Contains the main application logic.
│   ├── config.py             # Configuration file for the chatbot settings.
│   └── __pycache__/          # Compiled Python files for faster imports.
│
├── controllers/              # Handles incoming requests and interacts with the service.
│   └── chatbot_controller.py # Controller to manage chatbot interactions.
│
├── repositories/             # Manages data persistence and API calls.
│   └── openai_repository.py  # Handles interaction with OpenAI's API.
│
├── services/                 # Business logic and service layer.
│   └── chatbot_service.py    # Core service that processes chatbot requests.
│
├── utils/                    # Utility functions and helper files.
│   ├── openai_client.py      # Handles the client setup for OpenAI API interactions.
│   └── __init__.py           # Initializes the utils package.
│
├── Dockerfile                # Docker configuration for containerization.
├── requirements.txt          # Python dependencies for the project.
└── run.py                    # Main entry point to run the chatbot service.
```

### Folder Descriptions 📂
- **app/**: Contains the core application logic and configuration.
- **controllers/**: Manages incoming requests, invoking services and returning responses.
- **repositories/**: Responsible for interacting with external systems, such as the OpenAI API.
- **services/**: Contains the business logic for handling chatbot-related tasks.
- **utils/**: Provides utility functions, including setting up the OpenAI client.

## How to Deploy ⚙️
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Loony213/IA.git
   ```

2. **Install Dependencies:**
   Navigate to the project directory and install the necessary Python packages.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Chatbot:**
   - After setting up the environment and installing dependencies, run the chatbot service:
     ```bash
     python run.py
     ```

4. **Docker Deployment:**
   - Build the Docker image:
     ```bash
     docker build -t kamartinez/chatbot .
     ```
   - Run the container:
     ```bash
     docker run -p 5000:5000 kamartinez/chatbot
     ```

5. **Access the Service:**
   - The chatbot service will be available on `http://localhost:5000` once the container is running.

## Features ✨
- **AI-Powered Conversations**: Create chatbots that can generate intelligent and context-aware responses.
- **Integration with OpenAI**: Uses OpenAI's GPT models for conversational AI.
- **Modular Design**: The microservice is designed to be modular, allowing easy updates and scaling.

## License 📜
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
