import tkinter as tk
from tkinter import messagebox
import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'It\'s a tie!'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return 'You win!'
    else:
        return 'Computer wins!'

def play(player_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    messagebox.showinfo("Result", f"Computer chose: {computer_choice}\n{result}")

def create_app():
    app = tk.Tk()
    app.title("Rock-Paper-Scissors Game")

    tk.Label(app, text="Choose your option:", font=("Helvetica", 14)).pack(pady=10)

    tk.Button(app, text="Rock", command=lambda: play('rock'), font=("Helvetica", 12)).pack(pady=5)
    tk.Button(app, text="Paper", command=lambda: play('paper'), font=("Helvetica", 12)).pack(pady=5)
    tk.Button(app, text="Scissors", command=lambda: play('scissors'), font=("Helvetica", 12)).pack(pady=5)

    app.mainloop()

if __name__ == "__main__":
    create_app()
