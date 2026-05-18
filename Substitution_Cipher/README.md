# 🔐 Substitution Cipher - The Science of Secrecy ✉️

## 📌 Overview

This project is a Python-based implementation of a simple **Substitution Cipher Encryption System**.

The objective of this project is:

* to hide the original message
* using secret character substitution
* so that unauthorized people cannot understand the message

The project demonstrates the basic concept of:

## secure communication using cryptography

---

# 🧠 Project Story

Suppose Romeo wants to send a secret letter to Juliet.

However, the letter must pass through several people before reaching Juliet.

Romeo does not want anyone except Juliet to understand the message.

So instead of writing the original letters directly, Romeo uses:

* secret substituted letters
* encrypted text
* hidden communication

Juliet, knowing the secret substitution rule, can later decode the message.

This is the basic idea behind:

## 🔐 Substitution Cipher

---

# ⚙️ Working Principle

The project works in the following steps:

---

## ✅ Step 1: Read Original Message

The program reads a secret message from:

```text
ip_file.txt
```

Example:

```text
My dear Juliet
```

---

## ✅ Step 2: Create Cipher Mapping

The program creates a substitution dictionary using:

```python
string.ascii_letters
```

Each alphabet is replaced by its previous alphabet.

### Example Mapping

| Original | Encrypted |
|---|---|
| b | a |
| c | b |
| d | c |
| A | Z |
| a | Z |

---

## ✅ Step 3: Encrypt Each Character

The program reads the file:

* character by character

If the character exists in the cipher dictionary:

* it gets replaced with another secret character

Otherwise:

* spaces
* punctuation
* symbols

remain unchanged.

---

## ✅ Step 4: Generate Encrypted File

The encrypted message is written into:

```text
op_file.txt
```

---

# 🔒 Example Encryption

## Original Message

```text
My dear Juliet
```

## Encrypted Message

```text
Lx cdZq Itkhds
```

---

# 🎮 Features

* File-based encryption
* Character substitution system
* Secret communication simulation
* Automatic encrypted file generation
* Dictionary-based mapping
* Beginner-friendly cryptography logic

---

# 💻 Technologies Used

* Python
* File Handling
* Dictionaries
* String Module
* Loops and Conditional Statements

---

# 📁 Project Structure

```text
Substitution_Cipher/
│
├── code.py
├── ip_file.txt
├── op_file.txt
└── README.md
```

---

# ▶️ How to Run

## Step 1: Open terminal in project folder

## Step 2: Add your message inside

```text
ip_file.txt
```

## Step 3: Run the program

```bash
python code.py
```

---

# 📊 Sample Output

```text
Lx cdZq Itkhds
```

Encrypted message will also be stored in:

```text
op_file.txt
```

---

# 🧠 Concepts Used

* Cryptography Basics
* Substitution Cipher
* File Handling
* Dictionaries
* String Manipulation
* Character Encoding
* Python Loops

---

# 🎓 Learning Outcome

Through this project, one can learn:

* basic cryptography concepts
* secret communication systems
* file handling in Python
* dictionary-based mapping
* encryption techniques
* character substitution logic

---
# 🔐 Substitution Cipher - The Science of Secrecy ✉️

## 📌 Overview

This project is a Python-based implementation of a simple **Substitution Cipher Encryption System**.

The objective of this project is:

* to hide the original message
* using secret character substitution
* so that unauthorized people cannot understand the message

The project demonstrates the basic concept of:

## secure communication using cryptography

---

# 🧠 Project Story

Suppose Romeo wants to send a secret letter to Juliet.

However, the letter must pass through several people before reaching Juliet.

Romeo does not want anyone except Juliet to understand the message.

So instead of writing the original letters directly, Romeo uses:

* secret substituted letters
* encrypted text
* hidden communication

Juliet, knowing the secret substitution rule, can later decode the message.

This is the basic idea behind:

## 🔐 Substitution Cipher

---

# ⚙️ Working Principle

The project works in the following steps:

---

## ✅ Step 1: Read Original Message

The program reads a secret message from:

```text
ip_file.txt
```

Example:

```text
My dear Juliet
```

---

## ✅ Step 2: Create Cipher Mapping

The program creates a substitution dictionary using:

```python
string.ascii_letters
```

Each alphabet is replaced by its previous alphabet.

### Example Mapping

| Original | Encrypted |
|---|---|
| b | a |
| c | b |
| d | c |
| A | Z |
| a | Z |

---

## ✅ Step 3: Encrypt Each Character

The program reads the file:

* character by character

If the character exists in the cipher dictionary:

* it gets replaced with another secret character

Otherwise:

* spaces
* punctuation
* symbols

remain unchanged.

---

## ✅ Step 4: Generate Encrypted File

The encrypted message is written into:

```text
op_file.txt
```

---

# 🔒 Example Encryption

## Original Message

```text
My dear Juliet
```

## Encrypted Message

```text
Lx cdZq Itkhds
```

---

# 🎮 Features

* File-based encryption
* Character substitution system
* Secret communication simulation
* Automatic encrypted file generation
* Dictionary-based mapping
* Beginner-friendly cryptography logic

---

# 💻 Technologies Used

* Python
* File Handling
* Dictionaries
* String Module
* Loops and Conditional Statements

---

# 📁 Project Structure

```text
Substitution_Cipher/
│
├── code.py
├── ip_file.txt
├── op_file.txt
└── README.md
```

---

# ▶️ How to Run

## Step 1: Open terminal in project folder

## Step 2: Add your message inside

```text
ip_file.txt
```

## Step 3: Run the program

```bash
python code.py
```

---

# 📊 Sample Output

```text
Lx cdZq Itkhds
```

Encrypted message will also be stored in:

```text
op_file.txt
```

---

# 🧠 Concepts Used

* Cryptography Basics
* Substitution Cipher
* File Handling
* Dictionaries
* String Manipulation
* Character Encoding
* Python Loops

---

# 🎓 Learning Outcome

Through this project, one can learn:

* basic cryptography concepts
* secret communication systems
* file handling in Python
* dictionary-based mapping
* encryption techniques
* character substitution logic

---

# 🔮 Future Improvements

* Decryption Program
* Caesar Cipher Variation
* GUI Version
* Password-Protected Encryption
* Multiple Cipher Algorithms
* AES and RSA Introduction
* Secret Key Based Encryption

---

# ⭐ Conclusion

This project demonstrates a beginner-friendly implementation of a substitution cipher using Python. It combines cryptography fundamentals, file handling, dictionary mapping, and secret communication concepts into an interesting mini project.

---