import random

class Card:
    def __init__(self, colors, num, action = None):
        self.color = colors
        self.num = num
        self.action = action

    def __str__(self):
        return f"{self.color.capitalize()} {self.num}"
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.color == other.color and self.num == other.num
        return False

    
def parse_card():
    valid = False
    valid_colors = set(["Red", "Yellow", "Green", "Blue"])

    while valid != True:
        card = input(f'Select a card to play or type "draw" to draw a card. (ex. Red 8) ').strip().title()
        new_card = card.strip()
        if new_card == "Draw":
            valid = True
            return "Draw"
        elif "Skip" in new_card:
            split_card = new_card.split()
            if len(split_card) != 2:
                print("The card length you entered is either too short or too long. (ex. Red Skip)")
                new_card = input(f'Select a card to play or type "draw" to draw a card. ').strip().title()
                continue
            color = split_card[0]
            if color in valid_colors:
                valid = True
                return Card(color, None, action = "Skip" )
            else:
                print("That is not a valid color. Please enter a valid color. (Red, Yellow, Green, or Blue).")
        elif "Reverse" in new_card:
            split_card = new_card.split()
            if len(split_card) != 2:
                print("The card length you entered is either too short or too long. Try again. (ex. Blue Reverse) ")
                new_card = input(f'Select a card to play or type "draw" to draw a card. ').strip().title()
                continue
            color = split_card[0]
            if color in valid_colors:
                valid = True
                return Card(color, None, action = "Reverse")
            else:
                print("That is not a valid color. Please enter a valid color. (Red, Yellow, Green, or Blue).")
        elif "Draw Two" in new_card:
            split_card = new_card.split()
            if len(split_card) != 3:
                print("The card length you entered is either too short or too long. Try again. (ex. Red Draw Two)")
                new_card = input(f'Select a card to play or type "draw" to draw a card. ').strip().title()
                continue
            color = split_card[0]
            if color in valid_colors:
                valid = True
                return Card(color, None, action = "Draw Two")
            else:
                print("That is not a valid color. Please enter a valid color. (Red, Yellow, Green, or Blue).")   

        elif "Wild Card" in new_card:
            split_card = new_card.split()
            if len(split_card) !=2: 
                print("The card length you entered is either too short or too long. Try again. (ex. Wild Card) ")
                new_card = input(f'Select a card to play or type "draw" to draw a card. ').strip().title()
                continue
            if split_card[0] == "Wild":
                select_color = input("Select a color you would like to swap to: ")
                if select_color in valid_colors:
                    valid = True
                    return Card(select_color, None, action = "Wild Card" )
                else:
                    print("That is not a valid color. Please enter a valid color. Red, Yellow, Green, or Blue).")
        elif "Draw Four" in new_card:
            split_card = new_card.split()
            if len(split_card) !=2: 
                print("The card length you entered is either too short or too long. Try again. (ex. Draw Four) ")
                new_card = input(f'Select a card to play or type "draw" to draw a card. ').strip().title()
                continue
            if split_card[0] == "Draw":
                select_color = input("Select a color you would like to swap to: ")
                if select_color in valid_colors:
                    valid = True
                    return Card(select_color, None, action = "Draw Card" )
                else:
                    print("That is not a valid color. Please enter a valid color. Red, Yellow, Green, or Blue).")

        else:
            split_card = new_card.split()
            if len(split_card) != 2: 
                print("That is not a valid entry please try again.")
                new_card = input(f'Select a card to play or type "draw" to draw a card. (ex. Red 8) ').strip().title()
                continue
            color = split_card[0]
            num = split_card[1]
            valid_number = set(["0", "1", "2", "3", "4", "5", "6", "7",  "8", "9"])
            if color in valid_colors and num in valid_number:
                valid = True
                return Card(color, num)
            elif color not in valid_colors:
                print("That is not a valid color. Please enter a valid color and number (Red, Yellow, Green, or Blue).")
            elif num not in valid_number: 
                print("That is not a valid number. Pleae enter a card with a valid color and number (1-9).")
            else:
                print("That is not a valid card please try again.")



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
        #print("The faceup card on the table is:", starting_card)
        return starting_card
    
     

class Game:
    def __init__(self, current_face_up_card, players):
        self.current_face_up_card = current_face_up_card
        self.players = players

    def display(self):
        print(f"The current face up card is: {self.current_face_up_card}")
    
    def next_turn(self, deck):
        while not any(len(player.hand) == 0 for player in self.players):
            for player in self.players:
                print(f"The current face up card is: {self.current_face_up_card}")
                played_card = player.turn(deck, self.current_face_up_card)

                if played_card is not None:
                    self.current_face_up_card = played_card
                    deck.cards_played.append(played_card)

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

    def __init__(self, name, players):
        self.hand = []
        self.name = name
        self.players = players
    
    def draw(self, deck):
        self.hand.append(deck.cards.pop(0))

    def play(self): 
        player_choice = input(f'Select a card to play or type "draw" to draw a card. {[str(card) for card in self.hand]}')
        return player_choice
    
    def turn(self, deck, current_face_up_card):
        
        print(f"It is your turn {self.name}")

        print(f"Your hand is: {[str(card) for card in self.hand]}")    

        while True:
            player_choice = parse_card()
    
            if player_choice == "Draw":
                self.draw(deck)
                print(f"{self.name} has drawn a card")
                print(f"Updated hand {[str(card) for card in self.hand]}")
                print()
                return None
                
            elif player_choice in self.hand:
                if player_choice.color == current_face_up_card.color or player_choice.num == current_face_up_card.num:
                    print(f"{self.name} is playing {player_choice}") 
                    self.hand.remove(player_choice)

                    #checking to see if player has UNO
                    if len(self.hand) == 1:
                        print(f"{self.name} has UNO")
                    print(f"Updated hand {[str(card) for card in self.hand]}")
                    print()

                    #If not cards left player wins
                    if len(self.hand) == 0:
                        print(f"{self.name} has won! The game is over!")
                        return

                    #Reverse order of players
                    if "Reverse" in player_choice:
                       self.players.reverse()

                    #Makes the next player draw 2 cards and skips their turn
                    elif "Draw Two" in player_choice:
                        current_player_index = self.players.index(self)
                        next_player_index = (current_player_index+ 1) % len(self.players)
                        next_player = self.players[next_player_index]
                        print(f"{next_player.name} must draw 2 cards. And they cannot play a card")
                        next_player.draw(deck)
                        next_player.draw(deck)
                        print()

                    #Makes next player draw 4 and skips their turn
                    elif "Draw Four" in player_choice:
                        current_player_index = self.players.index(self)
                        next_player_index = (current_player_index+ 1) % len(self.players)
                        next_player = self.players[next_player_index]
                        print(f"{next_player.name} must draw 4 cards. And they cannot play a card")

                        #Loops to make player draw 4 cards
                        for _ in range(4):
                            next_player.draw(deck)
                        print()

                    #Skips the next players turn
                    elif "Skip" in player_choice:
                        current_player_index = self.players.index(self)
                        next_player_index = (current_player_index+ 1) % len(self.players)
                        next_player = self.players[next_player_index]
                        
                        
                        print(f"{next_player.name} has been skipped and will not play.")
                        print()
                        
                    
                    return player_choice
                else:
                    print("That is not a valid card to play. Please match the color or number of the card to the card on the.")
                    print(f"Your hand is: {[str(card) for card in self.hand]}") 
                    
            else:
                    print(f"Card {player_choice} is not in your hand! Try again.")
                    print(f"Your hand is: {[str(card) for card in self.hand]}") 
                    


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
        players_names = Player(name)
        players.append(players_names)
        count += 1

    
    deck = Deck()
    deck.shuffle()
    
    deck.deal(players)

    game = Game(deck.start(), players)

    game.next_turn(deck)
        
main()
