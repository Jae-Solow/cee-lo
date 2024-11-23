import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

import random
import sys
import tkinter as tk
from tkinter import messagebox

def roll_dice(num_dice=3):
    """Rolls the specified number of dice and returns a list of results."""
    return [random.randint(1, 6) for _ in range(num_dice)]

def evaluate_roll(dice):
    """Evaluates the dice roll and returns the outcome."""
    dice.sort()

    if dice == [4, 5, 6]:
        return "Automatic Win!"
    elif dice == [1, 2, 3]:
        return "Automatic Loss!"
    elif dice[0] == dice[1] == dice[2]:
        return "Triple, automatic win!"
    elif dice[0] == dice[1] or dice[1] == dice[2]:
        point = dice[0] if dice[0] != dice[1] else dice[2]
        return f"Point is: {point}"
    else:
        return "No point, roll again"
    
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.point = 0
        
    def roll(self):
        dice_roll = roll_dice()
        outcome = evaluate_roll(dice_roll)
        return dice_roll, outcome

    def update_score(self, outcome):
        if "Win" in outcome:
            self.score += 1
            return True
        elif "Loss" in outcome:
            return False
        else:
            if "No point" in outcome:
                self.point = 0
            else:
                try:
                    self.point = int(outcome.split()[-1])
                except ValueError:
                    pass
            return None
    
class CeeLoGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Cee-Lo Game")
        
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.current_player = self.player1
        
        self.label = tk.Label(root, text="Welcome to Cee-Lo! Game")
        self.label.pack()
        
        self.roll_button = tk.Button(root, text="Roll Dice", command=self.play_turn)
        self.roll_button.pack()
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
        
        self.score_label = tk.Label(root, text="Player 1: 0, Player 2: 0")
        self.score_label.pack()
        
        self.update_scores()
        
    def play_turn(self):
        dice_roll, outcome = self.current_player.roll()
        result = self.current_player.update_score(outcome)
        
        self.result_label.config(text=f"{self.current_player.name} rolled: {dice_roll}\nOutcome: {outcome}")
        
        if result is not None:
            if result:
                messagebox.showinfo("Round Result", f"{self.current_player.name} wins this round")
            else:
                messagebox.showinfo("Round Result", f"{self.current_player.name} loses this round")
            self.update_scores()
            self.switch_player()
        else:
            self.result_label.config(text=f"{self.current_player.name} rolled: {dice_roll}\nOutcome: {outcome}")
    
    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1 
        
    def update_scores(self):
        self.score_label.config(text=f"Scores:\nPlayer 1: {self.player1.score}\nPlayer 2: {self.player2.score}")
        
if __name__ == "__main__":
    root = tk.Tk()
    game = CeeLoGame(root)
    root.mainloop()