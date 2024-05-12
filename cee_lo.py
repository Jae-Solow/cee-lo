import random
import sys

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
def player_roll():
    """Prompt the player to roll the dice"""
    input("Press Enter to roll the dice")

def end_game():
    """Ends the game and exits the program."""
    print("Game Ended! Thanks for playing!")
    sys.exit()
    
def play_cee_lo():
    """Maintains the game loop and player interactions."""
    print("Welcome to Cee-lo!")
    print("The rules are simple: roll three dice and get a point value based on the outcome.")
    print("The player with the highest point value wins, unless there's a tie!")
    
    play_again = input("Play Cee-lo? (y/n): ").lower()
    if play_again != "y":
        return
    
    player1_score = 0
    player2_score = 0
    player2_point = 0
    while True:
        #Player 1's turn
        print("\nPlayer 1's turn!")
        player1_point = 0
        player_roll() # Player 1 rolls the dice
        dice_roll = roll_dice()
        print("You rolled:", dice_roll)
        outcome = evaluate_roll(dice_roll)
        print("Outcome:", outcome)
            
        if "Win" in outcome:
            player1_score += 1
            print("Player 1 wins this round!")
            break
        elif "Loss" in outcome:
            player2_score += 1
            print("Player 2 wins this round!")
            break
        else:
            if "No point" in outcome:
                player1_point = 0
                print("No point, roll again!")
            else:
                try:
                    player1_point = int(outcome.split()[-1])
                    print("Your point is", player1_point)
                except ValueError:
                    print("Invalid point value, Roll again!")
                    continue
                
        # Check for winner after both players roll
        if player1_score >= 3:
            print("\nPlayer 1 wins the game!")
            return
        elif player2_score >= 3:
            print("\nPlayer 2 wins the game!")
            return
        elif player1_point == player2_point:
            print("\nIt's a tie! Roll again!")
        else:
            if player1_point > player2_point:
                print("\nPlayer 1 has the higher point. Player 2 rolls again!")
            else:
                print("\nPlayer 2 has the higher point. Player 1 rolls again!")
        
        #Player 2's turn
        print("\nPlayer 2's turn!")    
        player2_point = 0
        player_roll() # Player 2 rolls the dice
        dice_roll = roll_dice()
        print("You rolled:", dice_roll)
        outcome = evaluate_roll(dice_roll)
        print("Outcome:", outcome)
            
        if "Win" in outcome:
            player2_score += 1
            print("Player 2 wins this round!")
        elif "Loss" in outcome:
            player1_score += 1
            print("Player 1 wins this round!")
        else:
            if "No point" in outcome:
                player1_point = 0
                print("No point, roll again!")
            else:
                try:
                    player2_point = int(outcome.split()[-1])
                    print("Your point is", player2_point)
                except ValueError:
                    print("Invalid point value, Roll again!")
                    continue
    
    # Check for input to end the game
    if input("Press 'q' to end the game").lower() == "q":
        end_game()
        
play_cee_lo()
