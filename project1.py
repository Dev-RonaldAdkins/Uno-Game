import random

def roll():
    min_vaule = 1
    max_value = 6
    roll = random.randint(min_vaule,max_value)
    
    return roll

#coninutes to ask the user for a valid number until it is true
while True:
    players = input("Enter the number of players (2-4): ")
    #determins if the value is a digit or not. If it is convert that number to an integer from string
    if players.isdigit():
        players = int(players)
        #checks to make sure it is a value of 2-4 if it is break out of the loop. Otherwise state it must be between 2 and 4 players.
        if 2<= players <= 4:  
            break
        else:
            print("Must be bewteen 2 - 4 players.")
    else:
        print("Invalid, Try again.")

max_score = 50
#puts 0 in list for each player there is
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    #looping over each player so they all get a turn
    for player_index in range(players):
        print("\nPlayer number", player_index + 1, "turn has just started!\n")
        print("Your total score is:", player_scores[player_index], "\n")
        current_score = 0

        #simulates a turn
        while True:
            should_roll = input("Would you like to roll (y)?")
            if should_roll.lower() != "y":
                break
            value = roll()
            
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a", value)
            print("Your score is:", current_score)
        
        player_scores[player_index] += current_score
        print("Your total score is:", player_scores[player_index])

max_score = max(player_scores)
winning_index = player_scores.index(max_score)

print("Player number", winning_index + 1, "is the winner with a score of:", max_score)

