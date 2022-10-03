# 1. The Shuffle
# write  a function get_shuffled_cards()
# Inside the function create  a 52-card list of tuples [("2", "diamonds ♦"), ("2", "hearts ♥"), ....., ("A", "spades ♠"), ("A", "clubs ♣")]

# The function returns a shuffled set of cards - the same list with tuples but shuffled!
# Find the correct method from built in random library.
# you can use a loop or use something from the library
# BONUS: Something can be useful from here: https://docs.python.org/3/library/itertools.html


import itertools
import random


def get_shuffled_cards(card_values, suits):
    card_deck = list(itertools.product(card_values, suits))
    shuffled_cards = random.sample(card_deck, k=52)
    print(shuffled_cards)
    return shuffled_cards


get_shuffled_cards(["2", "3", "4", "5", "6",
                   "7", "8", "9", "10", "J", "Q", "K", "A"], ["diamonds ♦", "hearts ♥", "spades ♠", "clubs ♣"])
