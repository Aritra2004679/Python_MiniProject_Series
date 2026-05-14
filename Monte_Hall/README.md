# 🎲 Monte Hall - 3 Doors and a Twist 🍫

## 📌 Overview

This project is a console-based probability game developed using Python based on the famous **Monty Hall Problem**.

The objective of the game is:

* to find the hidden chocolate
* among three different bags
* using logical decision making and probability

The game demonstrates how changing a player's decision after receiving a hint can statistically increase the probability of winning.

---

# 🧠 Game Concept

The game is inspired by the famous:

* Monty Hall Probability Problem
* Decision Making Theory
* Probability Simulation Logic

In this game:

* one bag contains a chocolate
* two bags contain goats
* the player initially selects one bag
* the admin opens one empty bag
* the player gets a second chance to:
  * stay with the original choice
  * or swap the choice

The project demonstrates that:

## swapping gives a higher probability of winning

---

# ⚙️ Working Principle

The game works in the following steps:

---

## ✅ Step 1: Create Three Bags

The program creates:

```text
Bag 1
Bag 2
Bag 3
```

Only one bag randomly contains the chocolate.

---

## ✅ Step 2: Player Chooses a Bag

The player selects one bag as the initial choice.

Example:

```text
Choose a door (0, 1, 2): 1
```

---

## ✅ Step 3: Admin Opens a Goat Bag

The admin opens one of the remaining bags that contains a goat.

Example:

```text
Admin opened door 2 showing a Goat.
```

The admin never opens:

* the player's selected bag
* the bag containing chocolate

---

## ✅ Step 4: Swap Decision

The player is asked:

```text
Do you want to swap? (Y/N):
```

The player can:

* stay with original choice
* swap to the remaining unopened bag

---

## ✅ Step 5: Final Result

The chosen bag is opened.

If chocolate is present:

```text
Player Wins!
```

Otherwise:

```text
Player Lost!
```

---

## ✅ Step 6: Statistics Display

The program stores:

* total swap wins
* total non-swap wins

Final statistics are displayed after all rounds.

---

# 🎮 Features

* Interactive gameplay
* Random chocolate placement
* Admin hint system
* Swap / No Swap decision logic
* Multiple rounds simulation
* Winning statistics display
* Console-based interaction

---

# 💻 Technologies Used

* Python
* Random Module
* Lists
* Loops and Conditional Statements

---

# 📁 Project Structure

```text
Monte_Hall/
│
├── code.py
└── README.md
```

---

# ▶️ How to Run

## Step 1: Open terminal in project folder

## Step 2: Run the program

```bash
python code.py
```

---

# 📊 Sample Output

```text
----- Round 1 -----
Choose a door (0, 1, 2): 0

Admin opened door 2 showing a Goat.

Do you want to swap? (Y/N): Y

Player Wins by Swapping!
```

---

# 📈 Example Final Result

```text
===== Final Results =====
Wins by Swapping     : 6
Wins without Swapping: 3
```

---

# 🧠 Concepts Used

* Randomization
* Probability Simulation
* Lists
* Loops
* Conditional Statements
* Decision Making Logic
* Console-Based Game Design

---

# 🎓 Learning Outcome

Through this project, one can learn:

* probability concepts in programming
* simulation-based logic
* randomization techniques
* game flow implementation
* decision-making algorithms
* Python console interaction

---

# ⭐ Conclusion

This project demonstrates the famous Monty Hall probability paradox using a simple and interactive Python console game. It combines probability theory, logical reasoning, randomization, and game simulation concepts into an engaging mini project.

---