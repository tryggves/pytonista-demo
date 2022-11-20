# See https://realpython.com/python-type-checking/#hello-types

import random
from typing import List, Tuple, Sequence, Any

SUITS = "♠ ♡ ♢ ♣".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

# Type aliases created as expressions
Card = Tuple[str, str]
Deck = List[Card]


# TYPE ALIAS
# Use type aliases to make code clear
def create_deck(shuffle: bool = False) -> Deck:
    """Create a new deck of 52 cards"""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)

    return deck


def deal_hands(deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""
    # Assign deck[0] and every 4th index (0, 4, 8, 12, ... to deck1
    deck1 = deck[0::4]
    # Assign deck[1] and every 4th index (1, 5, 9, 13, ... to deck2
    deck2 = deck[1::4]
    deck3 = deck[2::4]
    deck4 = deck[3::4]
    return deck1, deck2, deck3, deck4


def choose(items: Sequence[Any]) -> Any:
    """Choose and return a random item"""
    return random.choice(items)


def player_order(names: List[str], start: str = None):
    """Rotate player order so that start goes first"""
    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    return names[start_idx:] + names[:start_idx]


def play() -> None:
    """Play a 4-player card game"""
    deck = create_deck(shuffle=True)
    names = "Per Pål Espen Askeladd".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}
    start_player = choose(names)

    turn_order = player_order(names, start=start_player)

    # Randomly play cards from each player's hand until empty

    while hands[start_player]:

        for name in turn_order:
            card = choose(hands[name])
            hands[name].remove(card)
            print(f"{name}: {card[0] + card[1]:<3}  ", end="")
        print()


if __name__ == "__main__":
    play()
