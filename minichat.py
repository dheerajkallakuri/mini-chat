import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton
import openai
openai.api_key = "YOUR-API-KEY"


class ChatBotUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def chat_with_gpt(self, prompt):
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            max_tokens=50
        )
        return response.choices[0].message.content.strip()

    def init_ui(self):
        # Main widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layouts
        self.main_layout = QVBoxLayout(self.central_widget)
        self.text_layout = QHBoxLayout()

        # Text display area
        self.text_display = QTextEdit(self)
        self.text_display.setReadOnly(True)
        self.text_display.setStyleSheet("background-color: white;")

        # Text input field
        self.text_input = QLineEdit(self)
        self.text_input.setPlaceholderText("Type your message here...")

        # Send button
        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.handle_send_message)

        # Adding widgets to layout
        self.main_layout.addWidget(self.text_display)
        self.text_layout.addWidget(self.text_input)
        self.text_layout.addWidget(self.send_button)
        self.main_layout.addLayout(self.text_layout)

        # Window settings
        self.setWindowTitle("ChatBot")
        self.setGeometry(300, 300, 400, 500)

    def handle_send_message(self):
        user_message = self.text_input.text()
        if user_message:
            self.display_message(f'<span style="color: black;">{user_message}</span>')
            bot_reply = self.get_bot_reply(user_message)
            self.display_message(f'<span style="color: green;">{bot_reply}</span>')
            self.display_message(" ")
            self.text_input.clear()

    def display_message(self, message):
        self.text_display.append(message)

    def get_bot_reply(self, message):
        gpt_response = self.chat_with_gpt(message)
        return gpt_response


def main():
    app = QApplication(sys.argv)
    chat_bot_ui = ChatBotUI()
    chat_bot_ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
