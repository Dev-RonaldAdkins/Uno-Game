import random


class Card:
    def __init__(self, colors, num, action = None):
        self.color = colors
        self.num = num
        self.action = action

    def __str__(self):
        if self.action:
            return f"{self.color.capitalize() if self.color else ''} {self.action}"
        elif self.num:
            return f"{self.color.capitalize()} {self.num}"
        else:
            return "Invalid Card"

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.color == other.color and self.num == other.num and self.action == other.action
        return False

    
def parse_card():
    
    valid_colors = set(["Red", "Yellow", "Green", "Blue"])
 
 
    while True:
        card = input(f'Select a card to play or type "draw" to draw a card. (ex. Red 8) ').strip().title()
        card = card.strip()
        if card == "Draw":
            return "Draw"
        
        split_card = card.split()

        if card == "Wild Card":
                return Card(None, None, action = "Wild Card")
        elif card == "Draw Four":
            return Card(None, None, action = "Draw Four")     
        elif len(split_card) == 2:
            color, value = split_card

            if color in valid_colors and (value.isdigit() or value in ["Skip", "Reverse", "Draw"]):
                if value.isdigit():
                    return Card(color, value)
                return Card(color, None, action = value)   
            
        elif len(split_card) == 3:
            color, draw, two = split_card    
            if color in valid_colors and draw == "Draw" and two == "Two":
                return Card(color, None, action = "Draw Two")
        
        print("Invalid input. Please enter a card in the format 'Color Number' or 'Color Action'.")


class Deck:
    def __init__(self):
        self.cards = []
        self.cards_played = []
        color = ["Red", "Yellow", "Green", "Blue"]
        number = ["0", "1", "1", "2", "2", "3", "3", "4", "4", "5", "5", "6", "6", "7", "7", "8", "8", "9", "9"]
        wild = ["Wild Card", "Wild Card", "Wild Card", "Wild Card", "Draw Four", "Draw Four", "Draw Four", "Draw Four"]
        action = ["Skip", "Skip", "Draw Two", "Draw Two", "Reverse", "Reverse"]

        for colors in color:
            for num in number:
                self.cards.append(Card(colors,num))

        for colors in color:
            for actions in action:
                self.cards.append(Card(colors, None, actions))

        for wilds in wild:
            self.cards.append(Card(None, None, wilds))

          
    def shuffle(self):
        random.shuffle(self.cards)

    def full_deck(self):
        return [str(card) for card in self.cards]
    
    def deal(self, players, num_cards = 7):
      #print(f"Dealing cards to {len(players)} players")
      for player in players: 
       #print(f"Dealing cards to {player.name}")
       for _ in range(num_cards):
           #print(f"Adding card {self.cards[0]} to {player.name}")
           player.hand.append(self.cards.pop(0))
       

    def start(self):
        starting_card = self.cards.pop(0)
        self.cards_played.append(starting_card)
        #print("The faceup card on the table is:", starting_card
        return starting_card
    
    
     

class Game:
    def __init__(self, players, starting_card):
        self.current_face_up_card = starting_card
        self.players = players
    def __str__(self):
        if self.action:
            if self.color:
                return f"{self.color.captialize()} {self.action}"
            return f"{self.action}"
        elif self.num:
            return f"{self.color.caplitalize()} {self.num}"
        else:
            return "Invalid Card"

    def display(self):
        print(f"The current face up card is: {self.current_face_up_card}")
    
    def process_starting_card(self, deck):
        player_index = 0
        num_player = len(self.players)
        starting_card = self.current_face_up_card

        if starting_card.action == "Skip":
            print(f"{self.players[(player_index + 1) % num_player].name} has been skipped")
            player_index = (player_index + 2) % num_player
            return player_index

        elif starting_card.action == "Draw Four":
            next_player = self.players[(player_index + 1) % num_player]
            print(f"{self.players[(player_index + 1) % num_player].name} has to draw four cards and cannot play")
            for _ in range(4):
                    next_player.draw(deck)
            player_index = (player_index + 2) % num_player
            color_select = input("Choose a color you would like the card to be. (Red, Green, Blue, or Yellow)")     
            return player_index, color_select

        elif starting_card.action == "Wild Card":
            print(f"The starting card is {starting_card}. The first player will choose the starting color.")

            while True:
                color_select = input("Choose a color you would like the card to be. (Red, Green, Blue, or Yellow) ").capitalize() 
                if color_select in ["Red", "Green", "Blue", "Yellow"]:
                    starting_card.color = color_select
                    break
                print("Invalid color. Please choose Red, Green, Blue, or Yellow.")

            next_player = self.players[(player_index + 1) % num_player]
    
            return next_player, color_select

        elif starting_card.action == "Reverse":
            self.players.reverse()
            player_index = num_player - player_index - 1
            return player_index
        
        elif starting_card.action == "Draw Two":
            next_player = self.players[(player_index + 1) % num_player]
            print(f"{self.players[(player_index + 1) % num_player].name} has to draw two cards and cannot play")
            for _ in range(2):
                    next_player.draw(deck)
            player_index = (player_index + 2) % num_player
            return player_index

        else:
            player_index = (player_index + 1) % num_player
        
        return player_index
    
    def next_turn(self, deck, player_index=0):
        num_player = len(self.players)

        while not any(len(player.hand) == 0 for player in self.players):
            current_player = self.players[player_index]
            played_card = current_player.turn(deck, self.current_face_up_card)

            if played_card is not None:
                self.current_face_up_card = played_card
                deck.cards_played.append(played_card)

                if played_card.action == "Skip":
                    print(f"{self.players[(player_index + 1) % num_player].name} has been skipped")
                    player_index = (player_index + 2) % num_player

                elif played_card.action == "Draw Four":
                    next_player = self.players[(player_index + 1) % num_player]
                    print(f"{self.players[(player_index + 1) % num_player].name} has to draw four cards and cannot play")
                    for _ in range(4):
                            next_player.draw(deck)
                    player_index = (player_index + 2) % num_player      
                elif played_card.action == "Reverse":
                    self.players.reverse()
                    player_index = num_player - player_index - 1
                
                elif played_card.action == "Draw Two":
                    next_player = self.players[(player_index + 1) % num_player]
                    print(f"{self.players[(player_index + 1) % num_player].name} has to draw two cards and cannot play")
                    for _ in range(2):
                            next_player.draw(deck)
                    player_index = (player_index + 2) % num_player
                else:
                    player_index = (player_index + 1) % num_player
            else:
                player_index = (player_index + 1) % num_player

            if len(deck.cards) == 1:
                new_deck = []
                for cards in deck.cards_played:
                    if cards == self.current_face_up_card:
                        continue
                    new_deck.append(cards)
                deck.cards.extend(new_deck)
                deck.shuffle()
                deck.cards_played.clear()
                

class Player:

    def __init__(self, name, players=None):
        self.hand = []
        self.name = name
        self.players = players
    
    def draw(self, deck):
        self.hand.append(deck.cards.pop(0))

    def play(self): 
        player_choice = input(f'Select a card to play or type "draw" to draw a card. {[str(card) for card in self.hand]}')
        return player_choice
    
    def turn(self, deck, current_face_up_card):
        print()
        print(f"It is your turn {self.name}")

        print(f"Your hand is: {[str(card) for card in self.hand]}")    

        while True:
            player_choice = parse_card()
    
            if player_choice == "Draw":
                self.draw(deck)
                drawn_card = self.hand[-1]
                print(f"{self.name} has drawn a card")
                print(f"Updated hand {[str(card) for card in self.hand]}")
                #allows player to play card if it is playable.
                if drawn_card.color == current_face_up_card.color or drawn_card.num == current_face_up_card.num or drawn_card.action == current_face_up_card.action or drawn_card.action in ["Wild", "Draw Four"]:
                    print(f"{self.name}, you can play the card you just drew: {drawn_card}")
                    play_now = input("Would you like to play this card? (yes/no): ").strip().lower()

                    if play_now == "yes":
                        self.hand.remove(drawn_card)
                        print(f"{self.name} is playing {drawn_card}.")

                        if len(self.hand) == 1:
                            print(f"{self.name} has UNO!")

                        return drawn_card
                print(f"{self.name} cannot play the drawn card or chose not to play it.")
                print(f"The current face up card is: {current_face_up_card}")
                print()
                return None


            elif any(player_choice == card for card in self.hand):
                matching_card = next((card for card in self.hand if player_choice == card), None)

                if matching_card.action == "Draw Four":
                    matching_color_cards = [card for card in self.hand if card.color == current_face_up_card.color]
                    if matching_color_cards:
                        print("You cannot play a Draw Four while you have a card of the same color as the current faceup card")
                        continue
                    while True:
                        chosen_color = input("Select a color you would like to swap to (Red, Yellow, Green, or Blue). ").title()
                        if chosen_color in ["Red", "Yellow", "Green", "Blue"]:
                            matching_card.color = chosen_color
                            print(f"{self.name} is playing {matching_card.action} and the color is ({chosen_color}).")       
                            break
                        else:
                            print("Invalid color. Please choose Red, Yellow, Green, or Blue.")   
                        self.hand.remove(matching_card)  
                        return matching_card 


                if matching_card.action == "Wild Card":
                    while True:
                        chosen_color = input("Select a color you would like to swap to (Red, Yellow, Green, or Blue). ").title()
                        if chosen_color in ["Red", "Yellow", "Green", "Blue"]:
                            matching_card.color = chosen_color
                            print(f"{self.name} is playing {matching_card.action} and the color is ({chosen_color}).")       
                            break
                        else:
                            print("Invalid color. Please choose Red, Yellow, Green, or Blue.")   
                        self.hand.remove(matching_card)  
                        return matching_card 

                if (matching_card.color == current_face_up_card.color or matching_card.num == current_face_up_card.num or matching_card.action in ["Wild Card", "Draw Four"]):
                    print(f"{self.name} is playing {matching_card}.")
                    self.hand.remove(matching_card)

                    if len(self.hand) == 1:
                        print(f"{self.name} has UNO!")

                    elif len(self.hand) == 0:
                        print(f"{self.name} has won! The game is over!")
                        return

                    current_face_up_card.color = matching_card.color
                    current_face_up_card.num - matching_card.num
                    current_face_up_card.action = matching_card.action
                    print(f"The current face=up card is now {current_face_up_card}")       

                      

                    return matching_card
                print("That card doesn't match the current face-up card. Try again.")
            else:
                print(f"Card {player_choice} is not in your hand. Please try again.")

                  


def main():
  
    num_players = 0
    count = 0 
    players = []
    

    while num_players < 2 or num_players > 4:
        try:
            num_players = int(input("How many players? (2-4) "))
        except ValueError:
            print("Please enter an integer value.")

    while count < num_players:
        name = input("Enter player name: ")
        players.append(Player(name))
        count += 1


    deck = Deck()
    deck.shuffle()
    
    deck.deal(players)

    starting_card = deck.start()

    game = Game(players, starting_card)
    game.display()

    player_index = 0

    updated_state = game.process_starting_card(deck)

    # Use updated_player_index_or_state if it changes the game's starting state
    if isinstance(updated_state, tuple): # for cases with color selection
        player_index, color = updated_state
        print(f"starting color is {color}")
    elif isinstance(updated_state, int):
        player_index = updated_state
    

    game.next_turn(deck, player_index)
        
if __name__ == "__main__":
    main()