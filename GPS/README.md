# 🛰️ GPS Route Tracker using Python 🗺️

## 📌 Overview

This project is a Python-based GPS Route Tracking and Visualization system developed using:

* Python
* CSV File Handling
* Google Maps Plotting

The objective of this project is:

* to read latitude and longitude coordinates
* from a route file
* and visualize the travelling path on a map

The project simulates a basic:

## GPS Navigation and Route Tracking System

similar to real-world map applications.

---

# 🧠 Project Concept

Suppose a person is travelling in Kolkata from:

```text
Hotel → Destination
```

The travelling route contains multiple roadside coordinates.

The project:

* reads all GPS coordinates
* places markers on Google Maps
* connects the locations
* visualizes the travel route

This creates a simple simulation of:

* GPS tracking
* travel navigation
* route plotting systems

---

# ⚙️ Working Principle

The project works in the following steps:

---

## ✅ Step 1: Store Route Coordinates

The route is stored inside:

```text
route.txt
```

Each line contains:

```text
Latitude,Longitude
```

Example:

```text
22.5260,88.3660
22.5262,88.3663
22.5265,88.3666
```

These coordinates represent roadside travelling points.

---

## ✅ Step 2: Read Route File

The program uses:

```python
csv.reader()
```

to read all coordinates line by line.

---

## ✅ Step 3: Extract Latitude and Longitude

Each row is separated into:

* latitude
* longitude

using:

```python
lat = float(row[0])
long = float(row[1])
```

---

## ✅ Step 4: Store Route Coordinates

The coordinates are stored in:

```python
latitude_list
longitude_list
```

These lists are later used for route plotting.

---

## ✅ Step 5: Create Google Map

The project uses:

```python
gmplot.GoogleMapPlotter()
```

to generate an interactive Google Map.

---

## ✅ Step 6: Place GPS Markers

Different colored markers are used:

| Marker Color | Meaning |
|---|---|
| 🟡 Yellow | Starting Location |
| 🔵 Blue | Intermediate Route Points |
| 🔴 Red | Final Destination |

---

## ✅ Step 7: Connect Route Path

The program connects all coordinates using:

```python
gmap.plot()
```

This creates a GPS travel path.

---

## ✅ Step 8: Generate Interactive Map

Finally:

```python
gmap.draw("mymap.html")
```

creates:

```text
mymap.html
```

which opens in browser as an interactive GPS map.

---

# 🎮 Features

* GPS coordinate processing
* Route visualization
* Google Map integration
* Interactive HTML map generation
* Marker-based tracking
* Route path connection
* Realistic roadside plotting
* Beginner-friendly implementation

---

# 💻 Technologies Used

* Python
* CSV Module
* gmplot Library
* Google Maps
* File Handling
* Lists and Loops

---

# 📁 Project Structure

```text
GPS/
│
├── code.py
├── route.txt
├── mymap.html
└── README.md
```

---

# ▶️ Installation

## Step 1: Install gmplot

```bash
pip install gmplot
```

---

# ▶️ How to Run

## Step 1: Open terminal in project folder

```bash
cd GPS
```

---

## Step 2: Run the program

```bash
python code.py
```

---

## Step 3: Open Generated Map

After execution:

```text
mymap.html
```

will be generated.

Open it in browser.

---

# 📊 Sample Route File

```text
22.5260,88.3660
22.5262,88.3663
22.5265,88.3666
22.5268,88.3669
22.5271,88.3672
22.5274,88.3675
```

---

# 📊 Sample Output

## Terminal Output

```text
GPS Route Map Generated Successfully!
```

---

## Browser Output

The browser displays:

* 🟡 Starting Point
* 🔵 Connected Travel Route
* 🔴 Destination Point

on an interactive Google Map.

---

# 🧠 Concepts Used

* GPS Tracking
* Latitude and Longitude
* File Handling
* CSV Processing
* Map Visualization
* Route Plotting
* Google Maps Integration
* Python Libraries

---

# 🎓 Learning Outcome

Through this project, one can learn:

* how GPS systems work
* coordinate-based navigation
* route plotting techniques
* map visualization using Python
* file handling and CSV processing
* integration of external libraries

---

# ⚠️ Current Limitation

The project currently connects points using:

```text
straight-line plotting
```

instead of actual road navigation.

This happens because:

```python
gmap.plot()
```

only joins coordinates directly.

It does not use:

* Google Directions API
* real road intelligence
* traffic-aware navigation

---

# 🔮 Future Improvements

## 🚀 Advanced GPS Navigation

* Real Road Route Detection
* Google Directions API Integration
* Automatic Shortest Path Calculation
* Turn-by-Turn Navigation

---

## 🌍 Advanced Mapping Features

* Live GPS Tracking
* Real-Time Location Updates
* Traffic Visualization
* Satellite Map Support
* Zoom Controls

---

## 📱 User Experience Improvements

* GUI Version using Tkinter/PyQt
* Mobile App Integration
* Search Destination Feature
* Interactive Route Selection

---

## 🤖 Smart Features

* Voice Navigation
* Distance Calculation
* Estimated Time of Arrival (ETA)
* AI-Based Route Optimization

---

# ⭐ Conclusion

This project demonstrates a beginner-friendly GPS Route Tracking system using Python and Google Maps plotting. It combines GPS coordinates, file handling, route visualization, and map generation concepts into an interactive mini project.

The project serves as a strong introduction to:

* navigation systems
* geolocation technologies
* mapping applications
* GPS visualization techniques

---