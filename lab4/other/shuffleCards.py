import random

def shuffle_cards(coloda):
    random.shuffle(coloda)
    return coloda

def random_card(coloda):
    randomCard = random.choice(coloda)
    return randomCard

def find_key(my_dict, search_value):
    key = next((k for k, v in my_dict.items() if v == search_value), None)
    return key