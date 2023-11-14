import random 
from other.evklidGCD import EvklidGCD
from other.gen_evklid import GenEvklid
from other.coloda import coloda
from other.shuffleCards import shuffle_cards, random_card, find_key

class Player:
    def __init__(self, name) -> None:
        self.__name = name
        self.__c = 2
        self.__d = 2
        self.__hand = [0, 0]
        print(f"Добавление игрока {name}")
    
    @property
    def name(self):
        return self.__name
    
    @property
    def hand(self):
        return self.__hand
    
    @hand.setter
    def hand(self, hand):
        if hand[0]>0 and hand[1]>0:
            self.__hand = hand
        else:
            print("Недопустимая карта!")
    
    @property
    def c(self):
        return self.__c
    
    @property
    def d(self):
        return self.__d
    
    def print_hand_player(self):
        hand = self.__hand
        firstCard = find_key(coloda, hand[0])
        secondCard = find_key(coloda, hand[1])
        print(f" {self.__name}:\t{firstCard} {secondCard}")

    def printCD(self):
        return f"{self.__name}:\nC = {self.__c}\tD = {self.__d}"

    def generateCD(self, p):
        c = self.c
        d = self.d
        while (c*d)%(p-1) != 1:
            while True:
                c = random.randint(1, p-1)
                if EvklidGCD(p-1,c) == 1:
                    break
            U = GenEvklid(p-1,c)
            d = U[2]
            if d<0:
                d+=p
            self.__c = c
            self.__d = d


