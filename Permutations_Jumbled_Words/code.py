import random

def choose():
    words = [
        "python", "computer", "science", "programming",
        "developer", "keyboard", "algorithm", "function",
        "variable", "condition"
    ]
    return random.choice(words)


def jumble(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)


def thank(p1, p2, pp1, pp2):
    print("\nThanks for playing!")
    print(f"{p1}'s score: {pp1}")
    print(f"{p2}'s score: {pp2}")
    
    if pp1 > pp2:
        print(f"Congratulations {p1}, you won!")
    elif pp2 > pp1:
        print(f"Congratulations {p2}, you won!")
    else:
        print("It's a tie!")


def play():
    p1name = input('Player 1, Please enter your name: ')
    p2name = input('Player 2, Please enter your name: ')
    
    pp1 = 0
    pp2 = 0
    turn = 0

    while True:
        # computer's task
        picked_word = choose()

        # Create the question
        qn = jumble(picked_word)
        print("\nJumbled word:", qn)

        if turn % 2 == 0:
            # Player 1
            print(p1name, "Your turn.")
            ans = input('What is on my mind? ')
            
            if ans == picked_word:
                pp1 += 1
                print('Correct! Your score is:', pp1)
            else:
                print('Better luck next time. I thought:', picked_word)

        else:
            # Player 2
            print(p2name, "Your turn.")
            ans = input('What is on my mind? ')
            
            if ans == picked_word:
                pp2 += 1
                print('Correct! Your score is:', pp2)
            else:
                print('Better luck next time. I thought:', picked_word)

        c = int(input('Press 1 to continue and 0 to quit: '))
        if c == 0:
            thank(p1name, p2name, pp1, pp2)
            break

        turn += 1


# Start the game
play()
