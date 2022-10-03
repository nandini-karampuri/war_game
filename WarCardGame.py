from random import shuffle

# Ignore "double" wars
# Two useful variables for creating Cards.

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    def __init__(self):
        self.allcards=[(s,r) for s in SUITE for r in RANKS] #create a deck of cards

    def shuffle_cards(self):
        shuffle(self.allcards) #Shuffling the deck

    def split_in_half(self):
        return (self.allcards[:26],self.allcards[26:]) #split the shuffled deck in half and give to the players

class Hand:
    def __init__(self,cards):
        self.cards=cards

    def add_cards(self,added_cards):
        self.cards.extend(added_cards) #to add cards to the hand

    def remove_card(self):
        return self.cards.pop() #to remove cards from the hand

class Player(Hand):
    def __init__(self,name,hand):
        Hand.__init__(self,hand)
        self.name=name

    def play_card(self):
        drawn_card = self.remove_card()
        print("{} has placed: {}".format(self.name,drawn_card))
        print()
        return drawn_card

    def remove_war_cards(self):
        war_cards=[]
        if len(self.cards) <= 3:
            return war_cards
        else:
            for _ in range(3):
                war_cards.append(self.cards.pop(0))
            return war_cards

    def still_has_cards(self):
        return len(self.cards)!=0

print("Welcome to War, let's begin...")

d=Deck()
d.shuffle_cards()
h1,h2=d.split_in_half()
comp=Player("Computer",h1)

name=input("Enter Player name: ")
print()
user=Player(name,h2)
war_count=0
total_rounds = 0
# print(user.cards)
# print(comp.cards)
while user.still_has_cards() and comp.still_has_cards():
    total_rounds+=1
    print("Round = ",total_rounds)
    print("Here are the current standings: ")
    print(user.name+" count: "+str(len(user.cards)))
    print(comp.name+" count: "+str(len(comp.cards)))
    print("\nBoth players play a card!")
    print('\n')
    table_cards=[]
    #play a card
    p_card=user.play_card()
    c_card=comp.play_card()
    #add cards to the table_card
    table_cards.append(p_card)
    table_cards.append(c_card)

    if c_card[1]==p_card[1]:
        war_count+=1 #it's a war, play 3 cards by both the players
        print("It's a war!")
        print("Each player removes 3 cards 'face down' and then one card face up")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())
        #check 4th card ranks
        p_card=user.play_card()
        c_card=comp.play_card()
        table_cards.append(p_card)
        table_cards.append(c_card)
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.add_cards(table_cards)
        else:
            comp.add_cards(table_cards)
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.add_cards(table_cards)
        else:
            comp.add_cards(table_cards)
print("War count = ",war_count)
print("Total rounds = ",total_rounds)
if comp.still_has_cards():
    print("Computer won!")
if user.still_has_cards():
    print("{} won!".format(user.name))
