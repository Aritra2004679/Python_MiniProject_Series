# 🎂 Birthday Paradox Simulation using Python

## 📌 Overview

This project is a Python simulation of the famous probability problem known as the:

# Birthday Paradox

The objective of the program is to:

* Generate random birthdays for 50 candidates
* Store and display all birthdays
* Detect birthday collisions (same day and month)
* Demonstrate how surprisingly common shared birthdays are in a group

The program uses:

* Random number generation
* Date handling
* Leap year checking
* Collision detection logic

---

# 🧠 Theory Behind the Birthday Paradox

The Birthday Paradox is a famous concept in probability theory.

It states that:

> In a group of just 23 people, there is already more than a 50% chance that at least two people share the same birthday.

This result appears surprising because people often assume much larger groups are needed for birthday matches.

The paradox occurs because:

* the number of possible comparisons grows very quickly
* every new person can match with all previous people

For 50 people, the probability of at least one birthday collision becomes extremely high.

---

# ⚙️ Algorithm Used

The program randomly generates valid birthdays by checking:

* month
* leap year conditions
* correct number of days in each month

---

# 🔄 Detailed Step-by-Step Algorithm

## ✅ Step 1: Generate Random Year

A random year is selected between:

```text id="t6y23s"
1947 to 2026
```

---

## ✅ Step 2: Check Leap Year

A year is considered a leap year if:

* divisible by 4 and not divisible by 100
  OR
* divisible by 400

Algorithm:

```python id="m6jz0i"
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
```

---

## ✅ Step 3: Generate Random Month

A random month between:

```text id="l4vcg9"
1 to 12
```

is selected.

---

## ✅ Step 4: Generate Valid Day

### 🔹 February in Leap Year

Generate day from:

```text id="u5r4dt"
1 to 29
```

---

### 🔹 February in Non-Leap Year

Generate day from:

```text id="j7mpnh"
1 to 28
```

---

### 🔹 Months with 30 Days

For:

```text id="spg9t8"
April, June, September, November
```

Generate day from:

```text id="6lwhvl"
1 to 30
```

---

### 🔹 Months with 31 Days

For all remaining months:

```text id="9zjg6n"
1 to 31
```

---

## ✅ Step 5: Store Birthdays

The generated birthdays are stored in a list using:

```python id="rr0d4g"
datetime.date(year, month, day)
```

---

## ✅ Step 6: Detect Birthday Collisions

The program compares:

* day
* month

between every pair of candidates.

If both are equal:

```text id="2x1pru"
birthday collision found
```

The year is ignored because the Birthday Paradox considers only:

```text id="ztv4n8"
day + month
```

---

# 🚀 Features

* Random birthday generation
* Leap year handling
* Valid date generation
* Collision detection
* Birthday list display
* Birthday Paradox simulation

---

# 💻 How to Run

## ▶️ Run the Program

```bash id="ph7l9r"
python code.py
```

---

# 📊 Sample Output

```text id="d7o7rk"
List of Birthdays:

Candidate 1: 14/08/2002
Candidate 2: 12/03/1998
Candidate 3: 12/03/2005
Candidate 4: 25/11/1999
...

Birthday Collisions Found: 1

Repeated Birthdays:
12/03
```

---

# 📁 Project Structure

```text id="jv1znr"
Birthday_Paradox/
│
├── code.py
└── README.md
```

---

# 🧠 Concepts Used

* Random Module
* Datetime Module
* Probability Theory
* Leap Year Calculation
* Collision Detection
* Nested Loops
* Lists

---

# 🎓 Learning Outcome

Through this project, one can learn:

* How probability simulations work
* Randomized data generation
* Date validation techniques
* Birthday collision logic
* Real-world applications of probability theory

---

# ⭐ Conclusion

This project demonstrates the Birthday Paradox using Python by generating random birthdays and checking for birthday collisions among candidates. It provides practical insight into probability theory, collision detection, and simulation-based programming.

---
