
# 🔢 Magic Square Generator using Python

## 📌 Overview

This project generates a **Magic Square** of odd order using Python.

A Magic Square is a square matrix in which:

* The sum of every row is equal
* The sum of every column is equal
* The sum of both diagonals is also equal

The common sum obtained from every row, column, and diagonal is called the:

## 🎯 Magic Constant

---

# 🧠 Theory Behind Magic Square

A Magic Square is a special arrangement of numbers where mathematical symmetry is maintained throughout the matrix.

For a magic square of size:

$$
n \times n
$$

the magic constant is calculated using:

M=\frac{n(n^2+1)}{2}

Where:

* `n` = size of the square
* `M` = magic constant

---

## 📊 Example for n = 3

M=\frac{3(3^2+1)}{2}=15

Thus:

* Every row sum = 15
* Every column sum = 15
* Every diagonal sum = 15

Example Magic Square of size 3:

```text id="x7y1ya"
2 7 6
9 5 1
4 3 8
```

---

# ⚙️ Algorithm Used — Siamese Method

This project uses the **Siamese Method**, which is one of the most popular algorithms for generating odd-order magic squares.

The algorithm works only for:

## Odd values of `n`

---

# 🔄 Detailed Step-by-Step Algorithm

## ✅ Step 1: Create an Empty Matrix

Create an `n × n` matrix initialized with zeros.

Example for `n = 3`:

```text id="8b48kx"
0 0 0
0 0 0
0 0 0
```

---

## ✅ Step 2: Place Number 1

The first number (`1`) is placed at position:

```text id="s22cf8"
(n/2, n-1)
```

For `n = 3`:

```text id="5z9nrs"
(1, 2)
```

Matrix becomes:

```text id="d8bhp1"
0 0 0
0 0 1
0 0 0
```

---

## ✅ Step 3: Move Up and Right

After placing a number:

* move **one row up**
* move **one column right**

Mathematically:

```text id="hlq5o6"
i = i - 1
j = j + 1
```

---

## ✅ Step 4: Handle Boundary Conditions

### 🔹 Case 1: Row becomes -1

Wrap around to last row:

```text id="ttrj8r"
i = n - 1
```

---

### 🔹 Case 2: Column becomes n

Wrap around to first column:

```text id="l94s2g"
j = 0
```

---

### 🔹 Case 3: Both Conditions Occur Together

If:

```text id="eh4m2w"
i == -1 and j == n
```

then place the next number at:

```text id="g5r8r7"
(0, n-2)
```

---

## ✅ Step 5: Filled Cell Condition

If the target cell already contains a number:

* move down one row
* move left two columns

```text id="i79zxt"
i = i + 1
j = j - 2
```

---

## ✅ Step 6: Repeat

Continue until all numbers from:

```text id="cbgxhy"
1 → n²
```

are placed.

---

# 🚀 Features

* Generates odd-order magic squares
* Uses Siamese algorithm
* Accepts dynamic user input
* Displays magic constant
* Demonstrates matrix traversal and boundary handling

---

# 💻 How to Run

## ▶️ Run the Program

```bash id="p7wbof"
python code.py
```

---

# 📊 Sample Output

```text id="22fz5t"
Enter the size of magic square (odd number only): 5

Magic Square of Size 5

9 3 22 16 15
2 21 20 14 8
25 19 13 7 1
18 12 6 5 24
11 10 4 23 17

The sum of each row/column/diagonal is: 65
```

---

# 📁 Project Structure

Magic_Square
│
├── code.py
└── README.md

---

# 🧠 Concepts Used

* 2D Lists (Matrices)
* Nested Loops
* Conditional Statements
* Matrix Traversal
* Boundary Handling
* Mathematical Algorithms

---

# 🎓 Learning Outcome

Through this project, one can learn:

* How magic squares work mathematically
* Matrix manipulation using Python
* Algorithm implementation techniques
* Boundary condition handling
* Logical problem-solving

---

# ⭐ Conclusion

This project demonstrates how mathematical theory and algorithmic logic can be combined to generate a valid magic square using the Siamese method. It also helps in understanding matrix traversal, boundary handling, and structured problem-solving techniques in Python.

---
