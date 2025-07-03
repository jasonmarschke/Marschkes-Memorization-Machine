import sys
from PyQt5.QtWidgets import QApplication
from .flashcard_app import FlashcardApp


def main():
    cards = [
        {"prompt": "Hello", "answer": "Hola"},
        {"prompt": "Goodbye", "answer": "Adiós"},
    ]
    app = QApplication(sys.argv)
    window = FlashcardApp(cards)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
