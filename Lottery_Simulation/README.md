# 🎰 Lottery Simulation using Python 📈

## 📌 Overview

This project is a Python-based Lottery Simulation system that demonstrates:

* profit and loss calculation
* probability-based gaming
* account balance tracking
* graphical data visualization

The project simulates a lottery game played continuously for:

## 30 Days

where a player places a bet daily and checks whether the chosen number matches the lucky draw number.

The account balance changes dynamically based on:

* winning
* losing
* betting outcomes

The final result is visualized using a:

## Profit / Loss Graph

---

# 🧠 Project Concept

The game is based on a simple lottery simulation.

Every day:

* the player places a random bet number
* the system generates a lucky draw number

If both numbers match:

```text
Player Wins
```

Otherwise:

```text
Player Loses
```

The simulation helps visualize:

* gambling probability
* account fluctuations
* long-term profit/loss trends

---

# ⚙️ Working Principle

The project works in the following steps:

---

## ✅ Step 1: Start Lottery Simulation

The simulation starts with:

```python
account = 0
```

which represents the player's initial game account balance.

---

## ✅ Step 2: Simulate 30 Days

The game runs for:

```python
range(1, 31)
```

representing 30 continuous days of lottery betting.

---

## ✅ Step 3: Generate Random Bet Number

The player receives a random bet number between:

```text
1 to 10
```

using:

```python
random.randint(1, 10)
```

---

## ✅ Step 4: Generate Lucky Draw Number

The system generates another random number:

```text
Lucky Draw Number
```

between:

```text
1 to 10
```

---

## ✅ Step 5: Check Winning Condition

If:

```python
bet == lucky_draw
```

then:

```text
Player Wins
```

Otherwise:

```text
Player Loses
```

---

## ✅ Step 6: Update Account Balance

### Winning Condition

```python
account = account + 900 - 100
```

Meaning:

* ₹100 bet amount deducted
* ₹900 reward added

Net Profit:

```text
+ ₹800
```

---

### Losing Condition

```python
account = account - 100
```

Meaning:

```text
₹100 loss
```

---

## ✅ Step 7: Store Daily Account Balance

Daily balance values are stored inside:

```python
balance[]
```

for graph visualization.

---

## ✅ Step 8: Plot Profit/Loss Graph

The project uses:

```python
matplotlib.pyplot
```

to generate a graphical representation of:

* account growth
* losses
* winning spikes
* overall game trend

---

# 🎮 Features

* 30-day lottery simulation
* Random betting system
* Lucky draw generation
* Profit/Loss calculation
* Dynamic account balance tracking
* Graph visualization
* Probability-based gameplay
* Console-based interaction

---

# 💻 Technologies Used

* Python
* Random Module
* Matplotlib
* Lists
* Loops
* Conditional Statements

---

# 📁 Project Structure

```text
Lottery_Simulation/
│
├── code.py
└── README.md
```

---

# ▶️ Installation

## Install Matplotlib

```bash
pip install matplotlib
```

---

# ▶️ How to Run

## Step 1: Open terminal in project folder

## Step 2: Run the program

```bash
python code.py
```

---

# 📊 Sample Console Output

```text
Day 1
Your Bet      : 5
Lucky Draw    : 2
Result        : You Lost!
Game Account  : -100
-----------------------------------

Day 2
Your Bet      : 7
Lucky Draw    : 7
Result        : You Won!
Game Account  : 700
-----------------------------------
```

---

# 📈 Graph Output

The graph displays:

* X-axis → Days
* Y-axis → Account Balance

The graph visualizes:

* profit increase
* loss decrease
* fluctuations in account balance
* overall gambling trend

---

# 🧠 Concepts Used

* Probability Simulation
* Random Number Generation
* Data Visualization
* Profit and Loss Calculation
* Loops
* Lists
* Conditional Statements
* Graph Plotting

---

# 🎓 Learning Outcome

Through this project, one can learn:

* how lottery systems work
* probability-based simulations
* random number generation
* account balance tracking
* graphical data visualization
* basic financial analysis using Python

---

# ⚠️ Important Observation

This simulation demonstrates that:

* gambling outcomes are unpredictable
* losses can accumulate quickly
* probability affects long-term balance trends

The graph helps visualize real-world gambling risk behavior.

---

# 🔮 Future Improvements

## 🎲 Advanced Lottery Features

* User-based betting input
* Multiple ticket system
* Jackpot rewards
* Lucky number prediction

---

## 📈 Advanced Data Visualization

* Animated Graphs
* Bar Charts
* Real-Time Plot Updates
* Monthly and Yearly Analysis

---

## 💰 Financial Features

* Wallet System
* Deposit and Withdrawal
* Betting History
* Transaction Logs

---

## 🤖 Smart Features

* AI-Based Probability Analysis
* Winning Prediction Models
* Risk Analysis Dashboard
* Statistical Reports

---

## 🎮 Gameplay Enhancements

* GUI Version using Tkinter/PyQt
* Multiplayer Lottery System
* Sound Effects
* Online Lottery Simulation

---

# ⭐ Conclusion

This project demonstrates a simple yet effective lottery simulation system using Python. It combines probability concepts, random number generation, profit/loss tracking, and graphical visualization into an interactive mini project.

The project serves as a beginner-friendly introduction to:

* simulation systems
* gambling probability
* financial tracking
* graph visualization
* data analysis using Python

---