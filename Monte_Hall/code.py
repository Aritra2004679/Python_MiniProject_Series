import random

swap_wins = 0
stay_wins = 0

rounds = 10

for round_no in range(1, rounds + 1):

    print(f"\n----- Round {round_no} -----")

    # Create 3 doors
    doors = ["Goat", "Goat", "Goat"]

    # Randomly place chocolate behind one door
    chocolate_door = random.randint(0, 2)
    doors[chocolate_door] = "Chocolate"

    # Player chooses a door
    choice = int(input("Choose a door (0, 1, 2): "))

    # Admin opens a goat door
    possible_doors = []

    for i in range(3):
        if i != choice and doors[i] == "Goat":
            possible_doors.append(i)

    opened_door = random.choice(possible_doors)

    print(f"Admin opened door {opened_door} showing a Goat.")

    # Ask player whether to swap
    swap_choice = input("Do you want to swap? (Y/N): ").upper()

    # Determine remaining unopened door
    remaining_door = 0

    for i in range(3):
        if i != choice and i != opened_door:
            remaining_door = i

    # Swap if player wants
    if swap_choice == 'Y':
        choice = remaining_door

        if doors[choice] == "Chocolate":
            print("Player Wins by Swapping!")
            swap_wins += 1
        else:
            print("Player Lost after Swapping!")

    else:
        if doors[choice] == "Chocolate":
            print("Player Wins without Swapping!")
            stay_wins += 1
        else:
            print("Player Lost without Swapping!")

# Final Results
print("\n===== Final Results =====")
print("Wins by Swapping     :", swap_wins)
print("Wins without Swapping:", stay_wins)