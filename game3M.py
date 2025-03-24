from tkinter import *
from tkinter import ttk, messagebox, simpledialog
import random
import time
import pygame  # For sound effects
import os

class MysteryQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultimate Mystery Quiz")
        self.root.geometry("600x400")
        self.root.configure(bg="#2C3E50")
        
        pygame.mixer.init()
        self.click_sound = "click.wav" if os.path.exists("click.wav") else None
        self.win_sound = "win.wav" if os.path.exists("win.wav") else None
        
        self.i = 0
        self.score = 0
        
        self.questions = [
            {"question": "Choose a magical pet:", "options": ["Owl", "Cat", "Toad", "Snake"], "values": [1, 2, 3, 4]},
            {"question": "Which path would you walk down?", "options": ["Dark Alley", "Forest", "Castle Hallway", "Underwater Cave"], "values": [4, 3, 2, 1]},
            {"question": "What's your favorite class?", "options": ["Dark Arts", "Potions", "Herbology", "Charms"], "values": [1, 2, 4, 3]},
            {"question": "What would you do in a zombie apocalypse?", "options": ["Fight", "Run", "Hide", "Join Zombies"], "values": [4, 3, 2, 1]},
            {"question": "How do you handle conflict?", "options": ["Aggression", "Diplomacy", "Ignore", "Manipulate"], "values": [4, 3, 2, 1]},
            {"question": "Pick a superpower:", "options": ["Time Travel", "Mind Control", "Fire Powers", "Shape-shifting"], "values": [3, 4, 2, 1]},
        ]
        
        self.var = IntVar()
        self.create_widgets()
    
    def create_widgets(self):
        self.frame = Frame(self.root, bg="#34495E")
        self.frame.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        self.lbl_question = Label(self.frame, text="", font=("Arial", 14, "bold"), bg="#34495E", fg="white", wraplength=500)
        self.lbl_question.pack(pady=10)
        
        self.radio_buttons = []
        for i in range(4):
            rb = Radiobutton(self.frame, text="", variable=self.var, value=i+1, font=("Arial", 12), bg="#34495E", fg="white", activebackground="#2C3E50", activeforeground="yellow")
            rb.pack(anchor="w", padx=20)
            self.radio_buttons.append(rb)
        
        self.progress = ttk.Progressbar(self.root, orient=HORIZONTAL, length=500, mode='determinate')
        self.progress.pack(pady=10)
        
        btn_frame = Frame(self.root, bg="#2C3E50")
        btn_frame.pack(fill=X, pady=10)
        
        self.btn_prev = Button(btn_frame, text="Previous", command=self.previous, state=DISABLED, bg="#E74C3C", fg="white", font=("Arial", 12, "bold"), padx=10)
        self.btn_prev.pack(side=LEFT, expand=True, fill=X, padx=5)
        
        self.btn_next = Button(btn_frame, text="Next", command=self.next_question, bg="#27AE60", fg="white", font=("Arial", 12, "bold"), padx=10)
        self.btn_next.pack(side=LEFT, expand=True, fill=X, padx=5)
        
        self.btn_submit = Button(btn_frame, text="Submit", command=self.calculate_result, bg="#F39C12", fg="white", font=("Arial", 12, "bold"), padx=10)
        self.btn_submit.pack(side=LEFT, expand=True, fill=X, padx=5)
        self.btn_submit.pack_forget()
        self.btn_game = Button(self.root, text="Play Games", command=self.open_games, bg="#9B59B6", fg="white", font=("Arial", 12, "bold"), padx=10)
        self.btn_game.pack(fill=X, pady=10)
        self.load_question()
    
    def load_question(self):
        q = self.questions[self.i]
        self.lbl_question.config(text=q["question"])
        for j in range(4):
            self.radio_buttons[j].config(text=q["options"][j], value=q["values"][j])
        self.var.set(0)
        
        self.progress["value"] = ((self.i + 1) / len(self.questions)) * 100
    
    def play_sound(self, sound_file):
        if sound_file and os.path.exists(sound_file):
            pygame.mixer.Sound(sound_file).play()
    
    def next_question(self):
        self.play_sound(self.click_sound)
        if self.var.get() == 0:
            messagebox.showwarning("Warning", "Please select an answer before proceeding!")
            return
        
        self.score += self.var.get()
        self.i += 1
        
        if self.i == len(self.questions) - 1:
            self.btn_next.pack_forget()
            self.btn_submit.pack(fill=X, expand=True)
        
        self.btn_prev.config(state=NORMAL)
        self.load_question()
    
    def previous(self):
        self.play_sound(self.click_sound)
        if self.i > 0:
            self.i -= 1
            self.load_question()
        
        if self.i == 0:
            self.btn_prev.config(state=DISABLED)
        self.btn_next.pack(fill=X, expand=True)
        self.btn_submit.pack_forget()
    
    def calculate_result(self):
        self.play_sound(self.win_sound)
        
        result = ["Kind Soul 🌸", "Brave Warrior ⚔️", "Mastermind 🧠", "Dark Lord 😈"][min(self.score // 5, 3)]
        messagebox.showinfo("Quiz Result", f"Your Score: {self.score}\n{result}")
        time.sleep(1)
        self.root.destroy()
        
    def open_games(self):
        game_window = Toplevel(self.root)
        game_window.title("Game Selection")
        game_window.geometry("300x200")
        game_window.configure(bg="#34495E")
        
        Label(game_window, text="Choose a Game:", font=("Arial", 14, "bold"), bg="#34495E", fg="white").pack(pady=10)
        
        Button(game_window, text="Number Guessing Game", command=self.number_guessing_game, bg="#27AE60", fg="white", font=("Arial", 12)).pack(pady=5)
        Button(game_window, text="Rock-Paper-Scissors", command=self.rock_paper_scissors, bg="#E74C3C", fg="white", font=("Arial", 12)).pack(pady=5)
    
    def number_guessing_game(self):
        number = random.randint(1, 100)
        guess = None
        while guess != number:
            try:
                guess = int(simpledialog.askstring("Number Guessing Game", "Guess a number between 1 and 100:"))
                if guess < number:
                    messagebox.showinfo("Hint", "Too low! Try again.")
                elif guess > number:
                    messagebox.showinfo("Hint", "Too high! Try again.")
            except:
                break
        messagebox.showinfo("Result", f"Correct! The number was {number}.")
    
    def rock_paper_scissors(self):
        choices = ["Rock", "Paper", "Scissors"]
        user_choice = simpledialog.askstring("Rock-Paper-Scissors", "Enter Rock, Paper, or Scissors:")
        if user_choice not in choices:
            messagebox.showwarning("Invalid Choice", "Please enter Rock, Paper, or Scissors.")
            return
        
        comp_choice = random.choice(choices)
        
        result = ""
        if user_choice == comp_choice:
            result = "It's a Tie!"
        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
             (user_choice == "Paper" and comp_choice == "Rock") or \
             (user_choice == "Scissors" and comp_choice == "Paper"):
            result = "You Win!"
        else:
            result = "You Lose!"
        
        messagebox.showinfo("Result", f"You chose: {user_choice}\nComputer chose: {comp_choice}\n{result}")
    
if __name__ == "__main__":
    root = Tk()
    app = MysteryQuiz(root)
    root.mainloop()
