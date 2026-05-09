import string
import random


def dobble_game():

    symbols = list(string.ascii_letters)

    card1 = [0] * 5
    card2 = [0] * 5

    # Random positions for same symbol
    pos1 = random.randint(0, 4)
    pos2 = random.randint(0, 4)

    print("Common symbol positions:")
    print("Card 1 Position:", pos1)
    print("Card 2 Position:", pos2)

    # Choose same symbol
    same_symbol = random.choice(symbols)
    symbols.remove(same_symbol)

    # Place same symbol
    if pos1 == pos2:
        card1[pos1] = same_symbol
        card2[pos1] = same_symbol

    else:
        card1[pos1] = same_symbol
        card2[pos2] = same_symbol

        card1[pos2] = random.choice(symbols)
        symbols.remove(card1[pos2])

        card2[pos1] = random.choice(symbols)
        symbols.remove(card2[pos1])

    # Fill remaining positions
    i = 0
    while i < 5:

        if i != pos1 and i != pos2:

            alphabet1 = random.choice(symbols)
            symbols.remove(alphabet1)

            alphabet2 = random.choice(symbols)
            symbols.remove(alphabet2)

            card1[i] = alphabet1
            card2[i] = alphabet2

        i += 1

    # Display cards
    print("\nCard 1:", card1)
    print("Card 2:", card2)

    # User guess
    ch = input("\nSpot the similar symbol: ")

    if ch == same_symbol:
        print("Right!")
    else:
        print("Wrong!")
        print("Correct symbol was:", same_symbol)


# Function call
dobble_game()