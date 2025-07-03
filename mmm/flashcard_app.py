from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QLineEdit,
                             QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt


class FlashcardApp(QWidget):
    """Simple flashcard trainer."""

    def __init__(self, flashcards):
        super().__init__()
        self.flashcards = flashcards
        self.current_index = 0
        self.typing_mode = False

        self.prompt_label = QLabel()
        self.answer_label = QLabel()
        self.answer_label.hide()

        self.input_field = QLineEdit()
        self.input_field.returnPressed.connect(self.check_typed_answer)
        self.input_field.hide()

        self.show_button = QPushButton("Show Answer")
        self.show_button.clicked.connect(self.show_answer)

        self.known_button = QPushButton("Known")
        self.known_button.clicked.connect(self.mark_known)

        self.unknown_button = QPushButton("Unknown")
        self.unknown_button.clicked.connect(self.mark_unknown)

        self.typing_button = QPushButton("Typing Mode")
        self.typing_button.setCheckable(True)
        self.typing_button.clicked.connect(self.toggle_typing_mode)

        layout = QVBoxLayout()
        layout.addWidget(self.prompt_label)
        layout.addWidget(self.answer_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.show_button)
        btns = QHBoxLayout()
        btns.addWidget(self.known_button)
        btns.addWidget(self.unknown_button)
        btns.addWidget(self.typing_button)
        layout.addLayout(btns)
        self.setLayout(layout)

        self.update_card()

    def update_card(self):
        card = self.flashcards[self.current_index]
        self.prompt_label.setText(card['prompt'])
        self.answer_label.setText(card['answer'])
        self.answer_label.hide()
        self.input_field.clear()
        if self.typing_mode:
            self.input_field.show()
            self.show_button.hide()
        else:
            self.input_field.hide()
            self.show_button.show()

    def show_answer(self):
        self.answer_label.show()

    def mark_known(self):
        self.next_card()

    def mark_unknown(self):
        self.next_card()

    def toggle_typing_mode(self):
        self.typing_mode = self.typing_button.isChecked()
        self.update_card()

    def check_typed_answer(self):
        text = self.input_field.text().strip().lower()
        correct = self.flashcards[self.current_index]['answer'].strip().lower()
        if text == correct:
            self.mark_known()
        else:
            self.mark_unknown()

    def next_card(self):
        self.current_index = (self.current_index + 1) % len(self.flashcards)
        self.update_card()

    def keyPressEvent(self, event):
        if self.typing_mode and event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.check_typed_answer()
        else:
            super().keyPressEvent(event)
