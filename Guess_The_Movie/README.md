# 🎬 Guess The Movie Game using Python

## 📌 Overview

This project is a two-player console-based movie guessing game developed using Python.

The objective of the game is:

* to guess the hidden movie name
* by unlocking letters one by one
* within a limited number of attempts

The game randomly selects a movie name from a predefined list and displays it in:

## Fill-in-the-blank format

Players must strategically choose letters and try to identify the movie name with minimum clues.

---

# 🧠 Game Concept

The game is inspired by:

* word guessing games
* puzzle solving games
* hangman-style logic

Instead of revealing the complete movie name, the program:

* hides all letters using underscores (`_`)
* reveals letters only when correctly guessed
* gives players limited chances to unlock letters

After all chances are used, the player must:

## guess the complete movie name

---

# ⚙️ Working Principle

The game works in the following steps:

---

## ✅ Step 1: Player Registration

Two players enter their names.

Example:

```text
Player 1! Please enter your name:
Player 2! Please enter your name:
```

---

## ✅ Step 2: Random Movie Selection

The program randomly selects a movie name from the movie list using:

```python
random.choice(movies)
```

---

## ✅ Step 3: Create Hidden Question

The movie name is converted into blank spaces.

Example:

```text
Movie Name : dangal

Displayed As:

_ _ _ _ _ _
```

Spaces between words remain visible.

---

## ✅ Step 4: Letter Guessing

Players enter letters one by one.

If the letter exists in the movie name:

* the correct positions are unlocked
* updated blanks are displayed

Example:

```text
Your letter: a

_ a _ _ a _
```

---

## ✅ Step 5: Limited Chances

Each player receives:

```text
3 letter chances
```

This makes the game:

* more challenging
* more strategic
* more interesting

---

## ✅ Step 6: Final Movie Guess

After all chances are completed:

* player must guess the full movie name

If correct:

* score increases

Otherwise:

* correct movie name is displayed

---

## ✅ Step 7: Score Tracking

The program maintains:

* Player 1 score
* Player 2 score

Final scores are displayed when the game ends.

---

# 🎮 Features

* Two-player gameplay
* Random movie selection
* Hidden word generation
* Letter unlocking system
* Limited letter attempts
* Score tracking
* Turn-based gameplay
* Console interaction

---

# 💻 Technologies Used

* Python
* Random Module
* String Handling
* Loops and Conditional Statements

---

# 📁 Project Structure

```text
Guess_The_Movie/
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
Player 1! Please enter your name: Aritra
Player 2! Please enter your name: Rahul

Aritra Your turn

_ _ _ _ _ _

Chances left: 3

Your letter: d

d _ _ _ _ _

Chances left: 2

Your letter: a

d a _ _ a _

Chances left: 1

Your letter: n

d a n _ a _

Your final guess: dangal

Correct Answer!

Aritra Your Score is: 1
```

---

# 🧠 Concepts Used

* Randomization
* String Manipulation
* Functions
* Loops
* Conditional Statements
* Multiplayer Game Logic
* Console-Based UI

---

# 🎓 Learning Outcome

Through this project, one can learn:

* how multiplayer games work
* string handling in Python
* hidden word generation
* game logic implementation
* turn-based programming
* score management systems

---

# 🔮 Future Improvements

* Difficulty Levels
* Timer System
* Movie Categories
* Hints System
* Leaderboard
* GUI Version
* Database Connectivity
* Sound Effects

---

# ⭐ Conclusion

This project demonstrates a simple yet interactive movie guessing game using Python. It combines logic building, user interaction, randomization, and multiplayer gameplay mechanics into a fun console-based application.

---
