# ✊ Rock Paper Scissor Game using Python ✋✂️

## 📌 Overview

This project is a two-player console-based Rock Paper Scissor game developed using Python.

Unlike the traditional Rock Paper Scissor game, this version introduces a unique:

## 🔐 Secret Bit Selection Mechanism

Players enter:

* a secret number
* a secret bit position

The selected digit is processed using modulo operation to generate the final game choice.

This creates a fun combination of:

* game logic
* hidden strategy
* number manipulation

---

# 🧠 Game Concept

The game is inspired by the classic:

* Rock
* Paper
* Scissor

rules, but implemented using:

* secret numeric inputs
* bit-position logic
* modulo arithmetic

Each player secretly enters a number and selects a digit position from that number.

The chosen digit determines the player's move.

---

# ⚙️ Working Principle

The game works in the following steps:

---

## ✅ Step 1: Secret Number Input

Both players enter a secret number.

Example:

```text
Player 1, Enter your secret number : 45829
Player 2, Enter your secret number : 73164
```

---

## ✅ Step 2: Secret Bit Position Selection

Players choose a digit position from their secret number.

Example:

```text
Player 1, Enter the secret bit position : 2
Player 2, Enter the secret bit position : 1
```

---

## ✅ Step 3: Extract Secret Digit

The program extracts the digit from the selected position.

Example:

```python
int(num[bit_position])
```

---

## ✅ Step 4: Generate Game Choice

The extracted digit is converted into:

* Rock
* Paper
* Scissor

using:

```python
digit % 3
```

### Mapping Example

| Value | Choice |
|------|---------|
| 0 | Rock |
| 1 | Paper |
| 2 | Scissor |

---

## ✅ Step 5: Winner Determination

The program compares both player choices and displays:

* Player 1 Wins
* Player 2 Wins
* Draw

based on standard Rock Paper Scissor rules.

---

# 🎮 Features

* Two-player gameplay
* Secret number system
* Secret bit-position mechanism
* Rock Paper Scissor logic
* Input validation
* Continuous gameplay option
* Console-based interaction

---

# 💻 Technologies Used

* Python
* Dictionaries
* Functions
* Loops
* Conditional Statements
* String Indexing

---

# 📁 Project Structure

```text
Rock_Paper_Scissor/
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
===== Rock Paper Scissor Game =====

Player 1, Enter your secret number : 45829
Player 2, Enter your secret number : 73164

Player 1, Enter the secret bit position : 2
Player 2, Enter the secret bit position : 1

Player 1 Choice : Scissor
Player 2 Choice : Rock

Result : Player 2 Wins!
```

---

# 🧠 Concepts Used

* Functions
* Dictionaries
* String Manipulation
* Modulo Arithmetic
* Conditional Statements
* Game Logic
* Console-Based Programming

---

# 🎓 Learning Outcome

Through this project, one can learn:

* game logic implementation
* Python dictionaries
* string indexing
* modulo operations
* function-based programming
* multiplayer console interaction

---

# ⭐ Conclusion

This project demonstrates a creative implementation of the classic Rock Paper Scissor game using secret bit-position logic and number-based decision making. It combines Python fundamentals, hidden strategy mechanics, and multiplayer interaction into an engaging console-based game.

---