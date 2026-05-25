import random
import matplotlib.pyplot as plt

# Initial Account Balance
account = 0

# Lists for Graph
days = []
balance = []

print("===== Lottery Simulation Game =====\n")

# Simulation for 30 Days
for day in range(1, 31):

    # Store Day Number
    days.append(day)

    # Generate Random Bet and Lucky Draw
    bet = random.randint(1, 10)
    lucky_draw = random.randint(1, 10)

    print(f"Day {day}")
    print(f"Your Bet      : {bet}")
    print(f"Lucky Draw    : {lucky_draw}")

    # Winning Condition
    if bet == lucky_draw:

        print("Result        : You Won!")

        # Win Amount
        account = account + 900 - 100

    else:

        print("Result        : You Lost!")

        # Loss Amount
        account = account - 100

    # Store Account Balance
    balance.append(account)

    print(f"Game Account  : {account}")
    print("-" * 35)

# Final Account Balance
print("\n===== Final Result =====")
print("Amount in Game Account :", account)

# Graph Visualization
plt.figure(figsize=(10, 5))

plt.plot(days, balance,
         marker='o',
         linestyle='-')

# Graph Labels
plt.title("Lottery Simulation - Profit / Loss Over 30 Days")
plt.xlabel("Days")
plt.ylabel("Account Balance")

# Grid
plt.grid(True)

# Show Graph
plt.show()