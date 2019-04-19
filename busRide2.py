import random
import math
class Card(object):

    def __init__(self, rank, suit):
        self.rank = rank
        if suit == 1:
            self.suit = "Spades"
        elif suit == 2:
            self.suit = "Hearts"
        elif suit == 3:
            self.suit = "Clubs"
        elif suit == 4:
            self.suit = "Diamonds"

    def __str__(self):
        rank = self.rank
        if self.rank == 10:
            rank = "Jack"
        elif self.rank == 11:
            rank = "Queen"
        elif self.rank == 12:
            rank = "King"
        elif self.rank == 13:
            rank = "Ace"
        return str(rank) + " of " + self.suit
            

class Deck(object):

    def __init__(self):
        self.stack = []

    def fillStack(self):
        for s in range(1, 5):
            for r in range(2, 14):
                c = Card(r, s)
                self.stack += c

    def __str__(self):
        stack = []
        for c in self.stack:
            stack += str(c)
        return c

    def pickAndRemove(self):
        c = self.stack[random.randint(0, len(self.stack)-1)]
        self.stack.remove(c)
        return c

class BusRide(object):

    def __init__(self):
        self.start()

    def start(self):
        self.deck = Deck()
        self.tier1 = []
        self.tier2 = []
        self.tier3 = []
        self.tier4 = self.deck.pickAndRemove()
        self.done = False
        self.oneRank = 0
        self.twoRank = 0
        self.suits = []
        

        for i in range(4):
            self.tier1 += self.deck.pickAndRemove()

        for j in range(3):
            self.tier2 += self.deck.pickAndRemove()

        for k in range(2):
            self.tier3 = self.deck.pickAndRemove()

    def __str__(self):
        tier1 = []
        tier2 = []
        tier3 = []
        tier4 = str(self.tier4)

        for i in self.tier1:
            tier1 += str(i)
        for j in self.tier2:
            tier2 += str(j)
        for j in self.tier3:
            tier3 += str(k)
        return "Tier 4: " + tie4 + "\nTier 3: " + tier3 + "\nTier2: " + tier2 + "\nTier 1: " + tier1

    
    def status(self, correct):
        if correct:
            if self.tier != 4:
                print "Slick. Next tier."
            else:
                print "You got off the bus. Play again?"
                play = raw_input("'y' or 'n'")
                if play:
                    self.done = True
                    self.play()
                else:
                    print "Game over"
                    self.done = True
        else:
            print "You don't get off the bus until you win. Starting over"
            self.play()

    def play(self):
        self.start()
        
        
        print "Hop on the bus"
        print "Tier 1"
        
        t1 = self.tier1()
        self.status(t1)

        if self.done == False:
            print "Tier 2"
            t2 = self.tier2()
            self.status(t2)

        if self.done == False:
            print "Tier 3"
 
            self.status(self.tier3(card3, bool3))

        if self.done == False:
            print "Tier 4"
            bool4 = raw_input("Same or different suit? (type 's' or 'd')")
            self.status(self.tier4(self.tier4, bool4))

    def checkSuits(self):
        noOccurance = True
        lim = len(self.suits)-1
        count = 0
        while noOccurance or count < lim:
                noOccurance = self.suits[count] == self.tier4.suit
                count += 1
        return noOccurance
        

    def tier1(self):
        bool1 = raw_input("Red or black? (type 'r' or 'b')")
        card1 = raw_input("Which card? (pick from 0 to 3)")
        self.oneRank = self.tier1[card1].rank
        self.suits += self.tier1[card1].suit
        if bool1 == 'r':
            return self.tier1[card1].suit == "Hearts" or self.tier1[card1].suit == "Diamonds"
        elif bool1 == 'b':
            return self.tier1[card1].suit == "Spades" or self.tier1[card1].suit == "Clubs"

    def tier2(self):
        bool2 = raw_input("Higher or lower? (type 'h' or 'l')")
        card2 = raw_input("Which card? (pick from 0 to 2)")
        self.twoRank = self.tier2[card2].rank
        self.suits += self.tier2[card2].suit
        if bool2 == 'h':
            return self.oneRank <= self.tier2[card2].rank
        elif bool2 == 'l':
            return self.oneRank > self.tier2[card2].rank

    def tier3(self):
        bool3 = raw_input("Inside or outside? (type 'i' or 'o')")
        card3 = raw_input("Which card? (pick from 0 to 1)")
        self.suits += self.tier3[card3].suit
        if bool3 == 'i':
            return (self.oneRank >= card3.rank and self.twoRank < card3.rank) or (self.oneRrank < card3.rank and self.twoRank >= card3.rank)
        elif bool3 == 'o':
            return (self.oneRank > card3.rank and self.twoRank > card3.rank) or (self.oneRank < card3.rank and self.twoRank < card3.rank)


b = BusRide()
b.play()
    

    
        
        

    
            
        
        

