from classPlayer import Player
from other.simple_num import generate_simpleNum 
from other.fast_mult import fastMulty
from other.coloda import coloda
from other.shuffleCards import shuffle_cards, random_card, find_key
import os
import time
import logging

def log_function():
    open('game.log', 'w').close()
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='game.log') 
    global logger
    logger = logging.getLogger(__name__)

def consoleClear():
    os.system('clear')

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
        time.sleep(1)
    print("Игроки зарегестрированы!")
    time.sleep(1)
    consoleClear()
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
    logger.info(f'decode cards for: {player.name}')
    
def table_card_deal(colodaNow, players, p):
    tableCards = []
    for i in range(5):
        card = colodaNow[0]
        del colodaNow[0]
        for player in players:
            card = fastMulty(card, player.d,p)
        card = find_key(coloda, card)
        tableCards.append( card)
    logger.info(f'decode cards for table')
    return tableCards

def poker(players, p):
    shuffleCards = [x for x in range(2,54)]
    ### first step ###
    for player in players:
        shuffleCards = shuffle_cards(shuffleCards)
        logger.info(f'{player.name}: shuffled cards')
        shuffleCards = shifr_card(shuffleCards, player.c, p)
        logger.info(f'{player.name}: encode cards')
    ### second step ###
    deal_cards(players, shuffleCards)  
    ### third step ###
    for player in players:
        decode_card(player, players, p)
        player.print_hand_player()      
    ### table cards ###
    tableCards = table_card_deal(shuffleCards, players, p)
    print("table: ", end="")
    for i in tableCards:
        print(i, end=" ")
    print()
    logger.info(f"p = {p}")
    for player in players:
        logger.info(player.printCD())
        
def main():
    log_function()
    names = inpute_gamers()
    while names == None:
        consoleClear()
        print("Ошибка ввода пользователей, попробуйте ещё раз!")
        names = inpute_gamers()
    consoleClear()
    players, p = init_players(names) 
    poker(players, p)

if __name__=="__main__":
    main()