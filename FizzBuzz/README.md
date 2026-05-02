# FizzBuzz

## 📌 Problem Statement

Write a Python program that prints numbers from **1 to N** with the following conditions:

* If a number is divisible by **3**, print **Fizz**
* If a number is divisible by **5**, print **Buzz**
* If a number is divisible by both **3 and 5**, print **FizzBuzz**
* Otherwise, print the number itself

---

## 🚀 Approach

The solution uses a simple loop and conditional statements:

1. Iterate from `1` to `N`
2. Check divisibility using the modulo operator `%`
3. Print output based on conditions:

   * `i % 3 == 0 and i % 5 == 0` → FizzBuzz
   * `i % 3 == 0` → Fizz
   * `i % 5 == 0` → Buzz
   * Else → Number

---

## ▶️ How to Run

1. Make sure Python is installed
2. Open terminal in the project folder
3. Run the script:

```
python fizzbuzz.py
```

4. Enter a number when prompted

---

## 📊 Example Output

```
Enter the range: 15

1
2
3 = Fizz
4
5 = Buzz
6 = Fizz
7
8
9 = Fizz
10 = Buzz
11
12 = Fizz
13
14
15 = FizzBuzz
```

---

## 🧠 Concepts Used

* Functions
* Loops (`for`)
* Conditional statements (`if-elif-else`)
* Modulo operator (`%`)
* User input handling

---

## 📁 Project Structure

```
01-fizzbuzz/
│
├── fizzbuzz.py
└── README.md
```

---

## 🎯 Learning Outcome

This project helps in understanding:

* Basic problem-solving approach
* Writing clean and readable code
* Structuring a simple Python program

---

## 🚀 Future Improvements

* Return results as a list instead of printing
* Add input validation
* Implement a GUI or web-based version
* Write unit tests

---
