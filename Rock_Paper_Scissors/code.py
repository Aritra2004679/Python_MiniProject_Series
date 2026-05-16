def rock_paper_scissor(num1, num2, bit1, bit2):

    # Secret mappings for both players
    player_1 = {
        0: 'Rock',
        1: 'Paper',
        2: 'Scissor'
    }

    player_2 = {
        0: 'Paper',
        1: 'Rock',
        2: 'Scissor'
    }

    # Secret bit logic
    p1 = int(num1[bit1]) % 3
    p2 = int(num2[bit2]) % 3

    choice1 = player_1[p1]
    choice2 = player_2[p2]

    print(f"\nPlayer 1 Choice : {choice1}")
    print(f"Player 2 Choice : {choice2}")

    # Game Logic
    if choice1 == choice2:
        print("Result : Draw")

    elif (
        (choice1 == 'Rock' and choice2 == 'Scissor') or
        (choice1 == 'Paper' and choice2 == 'Rock') or
        (choice1 == 'Scissor' and choice2 == 'Paper')
    ):
        print("Result : Player 1 Wins!")

    else:
        print("Result : Player 2 Wins!")


# Main Program
while True:

    print("\n===== Rock Paper Scissor Game =====")

    num1 = input("Player 1, Enter your secret number : ")
    num2 = input("Player 2, Enter your secret number : ")

    bit1 = int(input("Player 1, Enter the secret bit position : "))
    bit2 = int(input("Player 2, Enter the secret bit position : "))

    # Validate bit positions
    if bit1 >= len(num1) or bit2 >= len(num2):
        print("\nInvalid Bit Position!")
        continue

    # Function Call
    rock_paper_scissor(num1, num2, bit1, bit2)

    # Continue Choice
    ch = input("\nDo you want to continue? (Y/N) : ").upper()

    if ch == 'N':
        print("\nGame Ended.")
        break