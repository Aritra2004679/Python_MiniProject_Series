# 🌐 Six Degrees of Separation

> A graph-based social network project that demonstrates the famous **Six Degrees of Separation Theory** using Python and NetworkX.

---

## 📌 Project Overview

The **Six Degrees of Separation** concept suggests that any two people in the world can be connected through a chain of no more than six social connections.

This project simulates that idea using a small social network where users can find the shortest connection path between themselves and a favourite person.

The project uses:

- Graph Theory
- Social Network Analysis
- Shortest Path Algorithms
- Data Visualization

---

## 🎯 Project Objective

The goal is to determine:

- Whether two people are connected
- The shortest chain of people connecting them
- The degree of separation between them
- A graphical representation of the network

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| NetworkX | Graph Creation & Analysis |
| Matplotlib | Network Visualization |
| VS Code | Development Environment |

---

## 📂 Project Structure

```text
Six_Degrees_of_Separation/
│
├── code.py
├── connections.txt
├── README.md
└── output_graph.png
```

---

## 📖 Dataset

The project uses a custom social network dataset stored in:

```text
connections.txt
```

Example:

```text
Aritra,Rahul
Aritra,Priya
Rahul,Aman
Rahul,Ritika
Priya,Neha
Neha,Hardik Pandya
Hardik Pandya,KL Rahul
KL Rahul,Virat Kohli
Anushka Sharma,Virat Kohli
```

Each line represents a connection between two people.

---

## ⚙️ Working Principle

### Step 1

Read all social connections from the file.

### Step 2

Create a graph where:

- Nodes = People
- Edges = Connections

### Step 3

Take user input:

```text
Enter your name
Enter favourite person
```

### Step 4

Use NetworkX shortest path algorithm to find the smallest connection chain.

### Step 5

Display:

- Connection path
- Degree of separation
- Graph visualization

---

## 🔄 Workflow

```text
Connections File
        │
        ▼
Create Graph
        │
        ▼
User Input
        │
        ▼
Shortest Path Search
        │
        ▼
Connection Found
        │
        ▼
Graph Visualization
```

---

## ▶️ Sample Execution

```text
==================================================
SIX DEGREES OF SEPARATION
==================================================

Enter your name: Aritra
Enter favourite person: Hardik Pandya

Connection Found!

Aritra
↓
Priya
↓
Neha
↓
Hardik Pandya

Degrees of Separation : 3
```

---

## 📊 Sample Graph Output

### Network Visualization

> Insert your graph screenshot below.

![Network Graph](output_graph.png)

---

## 🧠 Concepts Used

### Graph Theory

A social network is represented as a graph.

```text
Person → Node
Connection → Edge
```

Example:

```text
Aritra ─ Rahul
   │
 Priya
   │
 Neha
   │
Hardik Pandya
```

---

### Shortest Path

The shortest path algorithm identifies the minimum number of connections required to reach a target person.

Example:

```text
Aritra → Priya → Neha → Hardik Pandya
```

Degree of Separation:

```text
3
```

---

## 🌟 Features

✅ Simple social network simulation

✅ Graph visualization using NetworkX

✅ Finds shortest connection path

✅ Calculates degrees of separation

✅ Beginner-friendly implementation

✅ Real-world social network concept

---

## 🌍 Real-World Applications

### Social Media Analysis

Used in:

- Facebook
- LinkedIn
- Instagram

to recommend friends and connections.

### Professional Networking

Finding mutual connections between professionals.

### Recommendation Systems

Suggesting people, communities, or groups.

### Network Science

Studying how information spreads through society.

---

## ⚠️ Limitations

- Uses a small custom dataset
- Connections are manually created
- Not connected to real social media APIs
- Performance decreases with extremely large networks

---

## 🔮 Future Improvements

### 1. Stanford SNAP Facebook Dataset

Replace the custom dataset with:

```text
facebook_combined.txt
```

from Stanford SNAP to analyze a real social network.

---

### 2. Interactive Visualization

Use:

```python
PyVis
Plotly
```

for interactive graph exploration.

---

### 3. Friend Recommendation System

Recommend mutual friends based on graph connectivity.

---

### 4. Celebrity Reach Analysis

Calculate how many connections are needed to reach celebrities.

---

### 5. Graph Metrics

Implement:

- Degree Centrality
- Betweenness Centrality
- Clustering Coefficient
- Community Detection

---

### 6. GUI Application

Create a desktop application using:

- Tkinter
- PyQt

---

### 7. Web Application

Convert into:

- Flask App
- Streamlit App

for online interaction.

---

## 🎓 Learning Outcomes

Through this project, you will learn:

- Graph Theory Basics
- Network Analysis
- Shortest Path Algorithms
- Social Network Modeling
- NetworkX Library
- Data Visualization

---

## 🏆 Conclusion

This project demonstrates the practical implementation of the famous **Six Degrees of Separation Theory** using graph data structures and shortest path algorithms.

By representing people as nodes and relationships as edges, the program successfully discovers connection chains and visualizes social networks, providing a strong introduction to graph analytics and network science.

---

## 👨‍💻 Author

**Aritra Chakraborty**

Computer Science Engineering Student

⭐ If you found this project useful, consider giving it a star on GitHub.