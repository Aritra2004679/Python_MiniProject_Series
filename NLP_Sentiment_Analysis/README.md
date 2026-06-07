# 😊 Sentiment Analysis Using NLP

> A beginner-friendly Natural Language Processing project that analyzes the sentiment of text and classifies it as **Positive**, **Negative**, or **Neutral**.

---

## 📌 Project Overview

This project demonstrates a basic **Sentiment Analysis System** using **Natural Language Processing (NLP)** techniques in Python.

The program:

✅ Reads sentences from a text file
✅ Performs tokenization using NLTK
✅ Removes stopwords from the text
✅ Calculates sentiment polarity using TextBlob
✅ Classifies each sentence as Positive, Negative, or Neutral

---

## 🎯 Objectives

* 📖 Understand the fundamentals of NLP
* 🔤 Learn text preprocessing techniques
* 😊 Analyze sentiments in textual data
* 📊 Classify text based on polarity
* 💡 Gain hands-on experience with Python NLP libraries

---

## 🛠️ Technologies Used

| Technology  | Purpose                 |
| ----------- | ----------------------- |
| 🐍 Python   | Programming Language    |
| 📚 NLTK     | Text Preprocessing      |
| 💬 TextBlob | Sentiment Analysis      |
| 💻 VS Code  | Development Environment |

---

## 📂 Project Structure

```text
NLP_Sentiment_Analysis/
│
├── 📄 code.py
├── 📄 input.txt
├── 📄 README.md
└── 📄 requirements.txt
```

---

## ⚙️ NLP Workflow

```text
📄 Input File
      │
      ▼
🔤 Tokenization
      │
      ▼
🧹 Stopword Removal
      │
      ▼
💬 Sentiment Analysis
      │
      ▼
📊 Polarity Calculation
      │
      ▼
✅ Classification
      │
      ▼
📈 Output Result
```

---

## 📥 Sample Input

```text
I love this product.
The weather is wonderful today.
This movie is amazing.
I am very happy with the service.
The food tastes excellent.
I hate waiting in long queues.
This phone is terrible.
The experience was disappointing.
I am feeling sad today.
The room is okay.
```

---

## 🔍 Sentiment Categories

| Emoji | Sentiment | Polarity |
| ----- | --------- | -------- |
| 😊    | Positive  | > 0      |
| 😐    | Neutral   | = 0      |
| 😞    | Negative  | < 0      |

---

## 🚀 Installation

### 1️⃣ Install Required Libraries

```bash
pip install nltk textblob
```

### 2️⃣ Download NLTK Resources

```python
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
```

### 3️⃣ Run the Program

```bash
python code.py
```

---

## 📊 Sample Output

```text
Sentence 1: I love this product.

Tokens:
['I', 'love', 'this', 'product', '.']

Processed Text:
love product

Polarity:
0.5

Sentiment:
Positive 😊
```

---

## 🌟 Features

✨ Simple and beginner-friendly
✨ Uses NLP preprocessing techniques
✨ File-based input system
✨ Sentiment classification using TextBlob
✨ Easy to understand and modify

---

## 🎓 NLP Concepts Covered

* 🔤 Tokenization
* 🧹 Stopword Removal
* 📝 Text Processing
* 📊 Sentiment Analysis
* 💬 Polarity Detection

---

## 🌍 Real-World Applications

* 🛒 Product Review Analysis
* 📱 Social Media Monitoring
* 🏢 Brand Reputation Management
* 📈 Market Research
* 🗳️ Opinion Mining
* 🤖 Chatbots and Virtual Assistants

---

## ⚠️ Limitations

* ❌ Cannot accurately detect sarcasm
* ❌ Limited contextual understanding
* ❌ English language focused
* ❌ May misclassify complex sentences

---

## 🔮 Future Enhancements

* 🎨 GUI-based application
* 🌐 Multi-language support
* 🤖 Machine Learning models
* 🧠 Deep Learning (LSTM)
* 🚀 Transformer Models (BERT)
* 📊 Graphical sentiment visualization

---

## 🏆 Conclusion

This project demonstrates the implementation of **Sentiment Analysis using NLP** by combining **NLTK** for text preprocessing and **TextBlob** for sentiment classification. It provides a solid foundation for understanding opinion mining and real-world NLP applications.

---

## 👨‍💻 Author

**Aritra Chakraborty**
🎓 Computer Science Engineering Student

⭐ If you found this project useful, consider giving it a star!
