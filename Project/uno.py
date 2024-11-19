import random

class Card:
    def __init__(self, colors, num):
        self.color = colors
        self.num = num

    def __str__(self):
        return f"{self.color.capitalize()} {self.num}"
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.color == other.color and self.num == other.num
        return False
    
def prase_card():
    card = input(f'Select a card to play or type "draw" to draw a card. (ex. Red 8) ').strip().title()
    new_card = card.strip()
    if new_card == "Draw":
        return "Draw"
    else:
        split_card = new_card.split(" ")
        if len(split_card) > 2 or len(split_card) < 2: 
            print("That is not a valid entry please try again.") #Need to loop this later on to make sure this can be properly executed)
        color = split_card[0]
        num = split_card[1]
        valid_colors = set(["Red", "Yellow", "Green", "Blue"])
        if color in valid_colors:
            return Card(color, num)
        else:
            print("That is not a valid color.") #Need to loop this later to make sure they can correctly enter a valid color



class Deck:
    def __init__(self):
        self.cards = []
        color = ["Red", "Yellow", "Green", "Blue"]
        number = ["0", "1", "1", "2", "2", "3", "3", "4", "4", "5", "5", "6", "6", "7", "7", "8", "8", "9", "9"]
        #wild = ["wild card", "wild card", "wild card", "wild card", "draw four", "draw four", "draw four", "draw four"]
        #action = ["skip", "skip", "draw two", "draw two", "reverse", "reverse"]
        for colors in color:
            for num in number:
                self.cards.append(Card(colors,num))
        
         
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
        print("The faceup card on the table is:", starting_card)
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
                played_card = player.turn(deck)

                if played_card is not None:
                    self.current_face_up_card = played_card
                    self.display()
           
                  

class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name
    
    def draw(self, deck):
        self.hand.append(deck.cards.pop(0))

    def play(self): 
        player_choice = input(f'Select a card to play or type "draw" to draw a card. {[str(card) for card in self.hand]}')
        return player_choice
    
    def turn(self, deck):
        print(f"It is your turn {self.name}")
        if len(self.hand) == 1:
            print(f"{self.name} has UNO!")
        print(f"Your hand is: {[str(card) for card in self.hand]}")    

        while True:
            player_choice = prase_card()
                #f'Select a card to play or type "draw" to draw a card. {[str(card) for card in self.hand]}
            if player_choice == "Draw":
                self.draw(deck)
                print(f"{self.name} has drawn a card")
                return None
                #print(f"Updated hand {[str(card) for card in self.hand]}")
            elif player_choice in self.hand:
                print(f"{self.name} is playing {player_choice}") 
                self.hand.remove(player_choice)
                #print(f"Updated hand {[str(card) for card in self.hand]}")
                return player_choice
            else:
                print(f"Card {player_choice} is not in the hand!")


def main():


    num_players = int(input("How many players? (2-4) "))
    players = []
    count = 0
    while num_players < 2 or num_players > 4:
        num_players = int(input("Please enter a valid number of players (2-4)"))
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
