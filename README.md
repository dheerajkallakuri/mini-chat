# MiniChatBot using GPT-3.5

This is a simple GUI-based chatbot application built using PyQt5 and OpenAI's GPT-3.5 Turbo model. The application allows users to input a message, send it to the GPT model, and receive a response that is displayed in the chat interface.

<img width="413" alt="output" src="https://github.com/user-attachments/assets/d8e1a77d-0c29-4db9-ab4f-7e8c28e9134f">

## Features

- **Interactive Chat Interface**: Users can interact with the chatbot through a text input field and view responses in a text display area.
- **Simple Layout**: The application uses a clean and straightforward design with a text input field, a send button, and a display area for chat history.
- **OpenAI Integration**: The chatbot leverages OpenAI's GPT-3.5 Turbo model to generate responses based on user input.

## Setup

1. **Clone the Repository**:
   ```
   git clone https://github.com/your-repo/mini-chat.git
   cd mini-chat
   ```

2. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Add Your OpenAI API Key**:
   Replace `"YOUR-API-KEY"` in the code with your actual OpenAI API key. You can obtain an API key by signing up on [OpenAI's website](https://platform.openai.com/api-keys).

## Usage

1. **Run the Application**:
   ```
   python mini-chat.py
   ```

2. **Interacting with the ChatBot**:
   - Type your message in the input field at the bottom.
   - Click the "Send" button or press Enter to send the message.
   - The bot's response will be displayed in the chat display area.


## Notes

- Ensure your API key is kept secure and not shared publicly.
- The current implementation limits responses to 50 tokens. Adjust the `max_tokens` parameter in the `chat_with_gpt` function to modify this behavior.
- Try out other open source models by replacing the parameter `model` parameter in the `chat_with_gpt` function to modify this behavior.
