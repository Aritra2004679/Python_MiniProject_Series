# 🧠 Crowd Computing: Estimation using Wisdom of the Crowd

## 📌 Overview

This project demonstrates the concept of **Crowd Computing (Wisdom of the Crowd)** using a simple estimation problem.

A group of people is asked to estimate a quantity (e.g., number of gems in a jar). While individual guesses may vary, combining them using statistical methods often produces a result close to the actual value.

---

## 🎯 Objective

* Collect multiple estimates from users
* Compute aggregate estimates using statistical methods
* Compare results with the actual value
* Visualize the distribution of estimates

---

## 📁 Project Structure

```
PYTHON_NPTEL/
│
└── Crowd_Computing/
    ├── code1.py   # Basic estimation logic
    └── code2.py   # Visualization using matplotlib
```

---

## 🚀 Features

### 🔹 code1.py (Basic Approach)

* Takes crowd estimates as input
* Calculates:

  * Mean (Average)
  * Median
  * Trimmed Mean (removes outliers)
* Compares with actual value
* Displays error percentage

---

### 🔹 code2.py (Visualization)

* Plots histogram of all estimates
* Shows:

  * Actual value
  * Mean
  * Median
  * Trimmed Mean
* Helps visualize how crowd estimates are distributed

---

## ▶️ How to Run

### 1️⃣ Install dependencies

```bash
pip install matplotlib
```

### 2️⃣ Run basic estimation

```bash
python code1.py
```

### 3️⃣ Run visualization

```bash
python code2.py
```

---

## 📊 Example Use Case

* Estimating number of items in a jar
* Predicting values using crowd input
* Understanding effect of outliers on data

---

## 🧠 Concepts Used

* Mean (Average)
* Median
* Trimmed Mean
* Error Percentage
* Data Visualization (Histogram)
* Crowd Intelligence

---

## 🎓 Learning Outcome

* Understand how collective estimates improve accuracy
* Learn impact of outliers on statistical measures
* Gain hands-on experience with data visualization
* Apply theoretical concept of crowd computing in practice

---

## ⭐ Conclusion

This project shows that even if individual guesses are inaccurate, combining them intelligently can produce highly reliable results—highlighting the power of **crowd-based estimation**.

---
