import random

# List of movie names
movies = [
    'anand',
    'drishyam',
    'nayakan',
    'anbe sivam',
    'gol maal',
    'vikram veda',
    'black friday',
    'dangal',
    'titanic',
    'taare zameen par'
]


# Create question with blanks
def create_question(movie):

    qn = ""

    for char in movie:

        if char == " ":
            qn = qn + " "

        else:
            qn = qn + "_ "

    return qn


# Check whether letter is present
def is_present(letter, movie):

    if letter in movie:
        return True

    else:
        return False


# Unlock correctly guessed letters
def unlock(question, movie, letter):

    question_list = list(question)

    index = 0

    for char in movie:

        if char == letter:
            question_list[index * 2] = letter

        index += 1

    return "".join(question_list)


# Main game function
def play():

    p1name = input('Player 1! Please enter your name: ')
    p2name = input('Player 2! Please enter your name: ')

    pp1 = 0
    pp2 = 0

    turn = 0
    willing = True

    while willing:

        # Player 1 Turn
        if turn % 2 == 0:

            print("\n", p1name, "Your turn")

            picked_movie = random.choice(movies)

            question = create_question(picked_movie)

            print(question)

            modified_qn = question

            not_said = True

            chances = 3

            while not_said:

                print("Chances left:", chances)

                letter = input('Your letter: ').lower()

                if is_present(letter, picked_movie):

                    modified_qn = unlock(
                        modified_qn,
                        picked_movie,
                        letter
                    )

                    print(modified_qn)

                else:
                    print(letter, 'not found')

                chances = chances - 1

                # Final guess after chances end
                if chances == 0:

                    ans = input(
                        'Your final guess: '
                    ).lower()

                    if ans == picked_movie:

                        pp1 = pp1 + 1

                        print('Correct Answer!')

                        print(
                            p1name,
                            'Your Score is:',
                            pp1
                        )

                    else:

                        print('Wrong Answer!')

                        print(
                            'The movie was:',
                            picked_movie
                        )

                    not_said = False

            choice = input(
                '\nPress 1 to Continue or 0 to Quit: '
            )

            if choice == '0':

                print('\nFinal Scores')

                print(p1name, ':', pp1)
                print(p2name, ':', pp2)

                print('\nTHANKS FOR PLAYING!')

                willing = False

        # Player 2 Turn
        else:

            print("\n", p2name, "Your turn")

            picked_movie = random.choice(movies)

            question = create_question(picked_movie)

            print(question)

            modified_qn = question

            not_said = True

            chances = 3

            while not_said:

                print("Chances left:", chances)

                letter = input('Your letter: ').lower()

                if is_present(letter, picked_movie):

                    modified_qn = unlock(
                        modified_qn,
                        picked_movie,
                        letter
                    )

                    print(modified_qn)

                else:
                    print(letter, 'not found')

                chances = chances - 1

                # Final guess after chances end
                if chances == 0:

                    ans = input(
                        'Your final guess: '
                    ).lower()

                    if ans == picked_movie:

                        pp2 = pp2 + 1

                        print('Correct Answer!')

                        print(
                            p2name,
                            'Your Score is:',
                            pp2
                        )

                    else:

                        print('Wrong Answer!')

                        print(
                            'The movie was:',
                            picked_movie
                        )

                    not_said = False

            choice = input(
                '\nPress 1 to Continue or 0 to Quit: '
            )

            if choice == '0':

                print('\nFinal Scores')

                print(p1name, ':', pp1)
                print(p2name, ':', pp2)

                print('\nTHANKS FOR PLAYING!')

                willing = False

        # Change turn
        turn = turn + 1


# Start the game
play()