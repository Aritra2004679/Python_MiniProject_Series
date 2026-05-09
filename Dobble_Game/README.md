# 🎮 Dobble Game using Python

## 📌 Overview

This project is a simplified Python implementation of the popular pattern-recognition game:

## Dobble / Spot It!

In this game:

* Two cards are generated
* Each card contains 5 alphabet symbols
* Exactly one symbol is common between both cards
* The player must identify the matching symbol

The project demonstrates concepts of:

* Randomization
* Lists
* String manipulation
* Game logic
* Pattern matching

---

# 🧠 Theory Behind the Game

The core idea behind the Dobble game is:

> Any two cards share exactly one common symbol.

The player must visually compare both cards and quickly identify the matching symbol.

This project simulates that logic using:

* randomly generated alphabet symbols
* random card positions
* controlled placement of one common symbol

---

# ⚙️ Algorithm Used

## ✅ Step 1: Generate Symbols

All uppercase and lowercase English alphabets are stored using:

```python id="smg5d5"
string.ascii_letters
```

---

## ✅ Step 2: Create Two Cards

Two cards are created as lists:

```python id="zv03rq"
card1 = [0] * 5
card2 = [0] * 5
```

Each card can store 5 symbols.

---

## ✅ Step 3: Select Common Symbol Position

Random positions are generated for both cards:

```python id="9i2sl9"
pos1 = random.randint(0, 4)
pos2 = random.randint(0, 4)
```

These positions determine where the same symbol will appear.

---

## ✅ Step 4: Choose Common Symbol

A random alphabet symbol is selected:

```python id="eh2d4u"
same_symbol = random.choice(symbols)
```

This symbol is inserted into both cards.

---

## ✅ Step 5: Fill Remaining Positions

All remaining card positions are filled with unique random symbols so that:

* only one symbol remains common
* all others are different

---

## ✅ Step 6: Player Guess

The player is shown both cards and asked to identify the matching symbol.

If the answer is correct:

```text id="paz4qm"
Right!
```

Otherwise:

```text id="0p2rje"
Wrong!
```

---

# 🚀 Features

* Random card generation
* Exactly one matching symbol
* Interactive gameplay
* User input handling
* Uses Python functions and lists

---

# 💻 How to Run

## ▶️ Run the Program

```bash id="kxtjlwm"
python code.py
```

---

# 📊 Sample Output

```text id="gbnvg8"
Common symbol positions:
Card 1 Position: 1
Card 2 Position: 3

Card 1: ['a', 'X', 'm', 'P', 'q']
Card 2: ['t', 'B', 'y', 'X', 'L']

Spot the similar symbol: X
Right!
```

---

# 📁 Project Structure

```text id="k5w1yb"
Dobble_Game/
│
├── code.py
└── README.md
```

---

# 🧠 Concepts Used

* Functions
* Lists
* Loops
* Random Module
* String Module
* Pattern Matching
* Game Logic

---

# 🎓 Learning Outcome

Through this project, one can learn:

* Randomized game development
* List manipulation in Python
* Basic game design principles
* User interaction handling
* Logical thinking and pattern recognition

---

# ⭐ Conclusion

This project demonstrates how randomness and logical placement can be combined to create an engaging pattern-recognition game using Python. It also introduces important programming concepts through an interactive mini-game.

---
