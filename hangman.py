import requests, tkinter as tk
from tkinter import messagebox

class HangmanApp:
    def __init__(self):
        root = tk.Tk()
        root.title("Hangman Game")
        self.root = root

        self.word = self.get_random_word()
        self.guessed_letters = set()
        self.attempts_left = 6
        self.displayed_word = ["_"] * len(self.word)

        self.word_label = tk.Label(root, font=("Helvetica", 24))
        self.word_label.pack(pady=20)

        self.attempts_label = tk.Label(self.root, font=("Helvetica", 16))
        self.attempts_label.pack(pady=10)

        self.guessed_label = tk.Label(self.root, font=("Helvetica", 14))
        self.guessed_label.pack(pady=10)

        self.canvas = tk.Canvas(self.root, width=200, height=200)
        self.canvas.pack(pady=20)

        self.alphabet_buttons_frame = tk.Frame(self.root)
        self.alphabet_buttons_frame.pack(pady=20)

        self.alphabet_buttons = {}
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        for letter in self.alphabet:
            btn = tk.Button(
                self.alphabet_buttons_frame,
                text=letter.upper(),
                width=4,
                height=2,
                command=lambda letter=letter: self.guess(letter),
            )

            btn.grid(row=0, column=len(self.alphabet_buttons), padx=5, pady=5)
            self.alphabet_buttons[letter] = btn

        self.update_labels()
        self.root.mainloop()

    def get_random_word(self):
        url = "https://random-word-api.herokuapp.com/word"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data[0]
    
    def draw_hangman(self):
        if self.attempts_left == 5:  # Base
            self.canvas.create_line(50, 150, 150, 150, width=4)

        elif self.attempts_left == 4:  # Pole
            self.canvas.create_line(100, 150, 100, 50, width=4)

        elif self.attempts_left == 3:  # Crossbeam
            self.canvas.create_line(100, 50, 150, 50, width=4)

        elif self.attempts_left == 2:  # Head
            self.canvas.create_oval(130, 60, 170, 100, width=4)

        elif self.attempts_left == 1:  # Body
            self.canvas.create_line(140, 100, 140, 130, width=4)

        elif self.attempts_left == 0:  # Arms and Legs
            self.canvas.create_line(140, 130, 120, 170, width=4)  # Left Leg
            self.canvas.create_line(140, 130, 160, 170, width=4)  # Right Leg
            self.canvas.create_line(140, 110, 120, 90, width=4)   # Left Arm
            self.canvas.create_line(140, 110, 160, 90, width=4)   # Right Arm

    def end_game(self, won):
        for btn in self.alphabet_buttons.values():
            btn.config(state="disabled")

        if won:
            messagebox.showinfo("You Win!", f"Congratulations! You guessed the word '{self.word}' correctly!")
        else:
            messagebox.showinfo("Game Over", f"Game Over! The word was '{self.word}'.")  

    def update_displayed_word(self):
        self.displayed_word = [
            letter if letter in self.guessed_letters else "_"
            for letter in self.word
        ]

    def update_labels(self):
        self.word_label.config(text=" ".join(self.displayed_word))
        self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")
        self.guessed_label.config(text=f"Guessed Letters: {', '.join(sorted(self.guessed_letters))}")
    
    def guess(self, letter):
        if letter in self.guessed_letters:
            return

        self.guessed_letters.add(letter)

        if letter in self.word:
            self.update_displayed_word()
        else:
            self.attempts_left -= 1
            self.draw_hangman()

        self.update_labels()

        if self.attempts_left == 0:
            self.end_game(False)
        elif "_" not in self.displayed_word:
            self.end_game(True)