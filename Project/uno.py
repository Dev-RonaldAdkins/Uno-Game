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
        
        else:
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
        #print("The faceup card on the table is:", starting_card)
        return starting_card
    
    
     

class Game:
    def __init__(self, current_face_up_card, players):
        self.current_face_up_card = current_face_up_card
        self.players = players

    def display(self):
        print(f"The current face up card is: {self.current_face_up_card}")
    
    def next_turn(self, deck):
        player_index = 0
        num_player = len(self.players)

        while not any(len(player.hand) == 0 for player in self.players):
            current_player = self.players[player_index]
            print(f"The current face up card is: {self.current_face_up_card}")
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


            elif any(player_choice == card for card in self.hand):
                matching_card = next((card for card in self.hand if player_choice == card), None)

                if matching_card.action in ["Wild Card", "Draw Four"]:
                    while True:
                        chosen_color = input("Select a color you would like to swap to (Red, Yellow, Green, or Blue). ").title
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
                    return matching_card
                else:
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
        players_names = Player(name)
        players.append(players_names)
        count += 1

        for player in players:
            player.players = players

    
    deck = Deck()
    deck.shuffle()
    
    deck.deal(players)
    

    game = Game(deck.start(), players)

    game.next_turn(deck)
        
main()
