import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Game instructions
        self.instructions = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=('Arial', 16))
        self.instructions.pack(pady=10)

        # Buttons for choices
        self.rock_button = tk.Button(root, text="Rock", command=lambda: self.user_choice("Rock"), font=('Arial', 14))
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.user_choice("Paper"), font=('Arial', 14))
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.user_choice("Scissors"), font=('Arial', 14))
        self.scissors_button.pack(pady=5)

        # Result display
        self.result_label = tk.Label(root, text="", font=('Arial', 18), fg="blue")
        self.result_label.pack(pady=20)

        # Score tracking
        self.user_score = 0
        self.computer_score = 0

        self.score_label = tk.Label(root, text=f"Score - You: {self.user_score} | Computer: {self.computer_score}", font=('Arial', 14))
        self.score_label.pack(pady=10)

        # Play again button
        self.play_again_button = tk.Button(root, text="Play Again", command=self.play_again, font=('Arial', 14))
        self.play_again_button.pack(pady=10)

    def user_choice(self, user_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = self.determine_winner(user_choice, computer_choice)
        
        # Update scores
        if result == "You Win!":
            self.user_score += 1
        elif result == "You Lose!":
            self.computer_score += 1
        
        # Display choices and result
        self.result_label.config(text=f"You chose {user_choice}, Computer chose {computer_choice}.\n{result}")
        self.score_label.config(text=f"Score - You: {self.user_score} | Computer: {self.computer_score}")

    def determine_winner(self, user, computer):
        if user == computer:
            return "It's a Tie!"
        elif (user == "Rock" and computer == "Scissors") or \
             (user == "Scissors" and computer == "Paper") or \
             (user == "Paper" and computer == "Rock"):
            return "You Win!"
        else:
            return "You Lose!"

    def play_again(self):
        self.result_label.config(text="")
        self.score_label.config(text=f"Score - You: {self.user_score} | Computer: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
