# Marschkes-Memorization-Machine

This repository provides a small PyQt flashcard application.  The app
shows a prompt in one language and lets you reveal the translation or
type it yourself.

## Running

1. Install the dependencies (PyQt5):

   ```bash
   pip install PyQt5
   ```

2. Start the program:

   ```bash
   python -m mmm.main
   ```

## Typing Mode

Press the **Typing Mode** toggle button to enable typing mode.  The
application will display a text field where you can type the
translation.  Press Enter in that field to check your answer.  The app
will mark the card as known or unknown based on whether your typed
answer matches the expected translation (case-insensitive).
