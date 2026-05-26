# 🔤 Anagram Checker using Python

## 📌 Overview

This project is a simple Python program that checks whether two strings are:

## Anagrams

or not.

Two words are called anagrams if:

* they contain the same characters
* character frequencies are equal
* order of characters may differ

Examples:

```text
listen → silent
evil   → vile
```

The program accepts two strings from the user, sorts their characters, and compares them to determine whether they are anagrams.

---

# 🧠 Project Concept

The project demonstrates a simple string manipulation technique using Python.

The idea is:

* take two input strings
* convert both to lowercase
* sort the characters
* compare the sorted outputs

If both sorted strings are equal:

```text
They are Anagrams
```

Otherwise:

```text
They are not Anagrams
```

---

# ⚙️ Working Principle

The project works in the following steps:

---

## ✅ Step 1: User Input

The user enters two strings.

Example:

```text
Enter the first string : listen
Enter the second string : silent
```

---

## ✅ Step 2: Convert to Lowercase

Both strings are converted to lowercase using:

```python
str.lower()
```

This avoids case-sensitive comparison issues.

Example:

```text
Listen → listen
Silent → silent
```

---

## ✅ Step 3: Sort Characters

The program sorts all characters alphabetically using:

```python
sorted()
```

Example:

```text
listen → ['e', 'i', 'l', 'n', 's', 't']
silent → ['e', 'i', 'l', 'n', 's', 't']
```

---

## ✅ Step 4: Compare Sorted Strings

If both sorted lists are equal:

```python
sorted(str1) == sorted(str2)
```

then the strings are anagrams.

---

# 🎮 Features

* User input support
* Case-insensitive comparison
* Character sorting
* Anagram detection
* Beginner-friendly implementation
* Console-based interaction

---

# 💻 Technologies Used

* Python
* String Handling
* Sorting
* Conditional Statements

---

# 📁 Project Structure

```text
Anagrams/
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
Enter the first string : listen
Enter the second string : silent

['e', 'i', 'l', 'n', 's', 't']
['e', 'i', 'l', 'n', 's', 't']

These are Anagrams
```

---

# ❌ Non-Anagram Example

```text
Enter the first string : hello
Enter the second string : world

['e', 'h', 'l', 'l', 'o']
['d', 'l', 'o', 'r', 'w']

These are not Anagrams
```

---

# 🧠 Concepts Used

* String Manipulation
* Sorting
* User Input Handling
* Conditional Statements
* Case Conversion

---

# 🎓 Learning Outcome

Through this project, one can learn:

* how string comparison works
* sorting techniques in Python
* case-insensitive processing
* basic logic building
* beginner-friendly algorithm implementation

---

# ⚠️ Important Observation

The program converts both strings to lowercase before comparison because:

```text
Python string comparison is case-sensitive
```

Without lowercase conversion:

```text
Listen ≠ listen
```

---


# ⭐ Conclusion

This project demonstrates a simple and beginner-friendly implementation of an Anagram Checker using Python. It introduces important programming concepts like string manipulation, sorting, user input handling, and conditional logic.

The project serves as a strong beginner exercise for understanding:

* string processing
* comparison algorithms
* sorting operations
* logical problem solving using Python

---