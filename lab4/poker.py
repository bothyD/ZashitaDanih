from classPlayer import Player
from other.simple_num import generate_simpleNum 
from other.fast_mult import fastMulty
from other.coloda import coloda
from other.shuffleCards import shuffle_cards, random_card, find_key
import os
import time

def inpute_gamers():
    print("Введите имена игроков через пробел(1 < кол-во < 10):")
    names = input()
    names = names.split(" ")
    nPlayers = len(names)
    if nPlayers >9 or nPlayers < 2:
        return None
    else:
        return names

def init_players(names):
    p = generate_simpleNum()
    players = []
    for name in names:
        player = Player(name)
        player.generateCD(p)
        players.append(player)
        # time.sleep(2)
    print("Игроки зарегестрированы!")
    # time.sleep(2)
    os.system('clear')
    return players, p

def shifr_card(cards, c, p):
    i = 0
    for card in cards:
        u = fastMulty(card,c,p)
        cards[i] = u
        i+=1
    return cards

def deal_cards(players, coloda):
    for player in players:
        handPlayer = []
        card = random_card(coloda)
        handPlayer.append(card)
        del coloda[0]
        card = random_card(coloda)
        handPlayer.append(card)
        del coloda[1]
        player.hand = handPlayer

def decode_card(player, players, p):
    for play in players:
        if play != player:
            playerHand = player.hand
            firstCard = fastMulty(playerHand[0], play.d,p)
            secondCard = fastMulty(playerHand[1], play.d,p)
            playerHand =[firstCard, secondCard]
            player.hand = playerHand
    playerHand = player.hand
    firstCard = fastMulty(playerHand[0], player.d,p)
    secondCard = fastMulty(playerHand[1], player.d,p)
    playerHand =[firstCard, secondCard]
    player.hand = playerHand
    

def poker(players, p):
    shuffleCards = [x for x in range(2,54)]
    ### first step ###
    for player in players:
        shuffleCards = shuffle_cards(shuffleCards)
        shuffleCards = shifr_card(shuffleCards, player.c, p)
    
    ### second step ###
    deal_cards(players, shuffleCards)  
    
    ### third step ###
    for player in players:
        decode_card(player, players, p)
        player.print_hand_player()
    
    

def main():
    names = inpute_gamers()
    while names == None:
        os.system('clear')
        print("Ошибка ввода пользователей, попробуйте ещё раз!")
        names = inpute_gamers()
    os.system('clear')
    players, p = init_players(names) 
    poker(players, p)

if __name__=="__main__":
    main()