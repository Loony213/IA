
# IA Repository 🤖

This repository is part of the **IA** domain and contains microservices that are used to create chatbots with the help of the OpenAI library. The chatbot service allows users to create AI-powered conversational agents that can interact and respond to various inputs in a human-like manner.

## Repository Link 📁
- [GitHub Repository](https://github.com/Loony213/IA)

## Purpose 🎯
The primary purpose of this repository is to provide a set of tools and microservices that enable the creation of chatbots using OpenAI's models. These chatbots can be customized and integrated into various platforms, providing conversational AI capabilities.

## Features ✨
- **Chatbot Creation**: The repository includes all the necessary components to create a functional chatbot using the OpenAI library.
- **Integration with OpenAI**: Uses OpenAI's GPT models to enable intelligent and context-aware conversations.
- **Microservice Architecture**: The repository follows a microservices architecture, making it easy to scale, manage, and integrate with other services.

## Technologies 💻
- **Programming Language**: Python 3.x
- **Library**: OpenAI API
- **Containerization**: Docker (optional)

## Project Structure 🧑‍💻
The repository is structured as follows:

```
IA/
├── .github/workflows/         # Contains GitHub Actions workflows for continuous integration.
│   └── bug_code              # Workflow configuration for handling bug-related code.
│
├── chatbot/                   # Contains the chatbot microservice logic.
│   └── chatbot.py             # Main script to interact with OpenAI API and create the chatbot.
│
├── README.md                  # This file.
└── requirements.txt           # Python dependencies for the project.
```

### Folder Descriptions 📂
- **.github/workflows/**: Contains workflow configurations for GitHub Actions to automate tasks like building and testing.
- **chatbot/**: Contains the logic for creating and configuring the chatbot.
- **requirements.txt**: Lists the required Python libraries, including the OpenAI library for interacting with GPT models.

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
     python chatbot/chatbot.py
     ```

4. **Access the Service:**
   - The chatbot will be available for interaction via the configured method in the `chatbot.py` script.

## License 📜
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
