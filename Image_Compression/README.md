# 🖼️ Image Compression using Python

## 📌 Overview

This project demonstrates a simple **Image Compression** technique using **Python**, **NumPy**, and **Pillow (PIL)**.

The image is first converted to grayscale and then compressed by reducing the number of intensity levels from **256 grayscale values** to only **8 quantized levels**. This process reduces the amount of information required to represent the image while preserving its overall visual appearance.

---

## 🚀 Features

✅ Load and process grayscale images

✅ Perform pixel-level image manipulation

✅ Reduce 256 grayscale levels to 8 intensity levels

✅ Generate a compressed image automatically

✅ Convert images into NumPy arrays for analysis

✅ Demonstrate a basic lossy image compression technique

---

## 🛠️ Technologies Used

| Technology       | Purpose                   |
| ---------------- | ------------------------- |
| 🐍 Python        | Core Programming Language |
| 🔢 NumPy         | Numerical Computing       |
| 🖼️ Pillow (PIL) | Image Processing          |

---

## 📂 Project Structure

```text
Image_Compression/
│
├── code.py
├── lena.jfif
├── lena_2.jpg
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

The grayscale intensity range (0–255) is divided into **8 equal intervals**:

| Original Pixel Range | Quantized Value |
| -------------------- | --------------- |
| 0 – 31               | 0               |
| 32 – 63              | 1               |
| 64 – 95              | 2               |
| 96 – 127             | 3               |
| 128 – 159            | 4               |
| 160 – 191            | 5               |
| 192 – 223            | 6               |
| 224 – 255            | 7               |

### 🔄 Compression Process

```text
Original Image
       │
       ▼
Convert to Grayscale
       │
       ▼
Read Pixel Values
       │
       ▼
Quantize Intensities
       │
       ▼
Generate Compressed Image
       │
       ▼
Save Output Image
```

---

## 💻 Installation

Clone the repository:

```bash
git clone <repository-url>
cd Image_Compression
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the project:

```bash
python code.py
```

After execution:

```text
Compressed image shape: (height, width)
Compression completed successfully!
```

The compressed image will be saved as:

```text
lena_2.jpg
```

---

## 📊 Compression Concept

### Before Compression

* 🎨 256 grayscale levels
* 📈 Higher image detail
* 💾 More information stored

### After Compression

* 🎨 Only 8 grayscale levels
* 📉 Reduced image detail
* 💽 Less information stored
* ⚡ Simpler image representation

---

## 🎯 Learning Outcomes

By completing this project, you will learn:

* 🖼️ Fundamentals of Digital Image Processing
* 🎨 Grayscale Image Representation
* 🔢 Pixel-Level Manipulation
* 📉 Intensity Quantization
* 💾 Lossy Compression Techniques
* 🐍 NumPy and Pillow Integration
* 📊 Image Data Analysis

---

## 🔮 Future Enhancements

* 🎨 Color Image Compression
* 📊 Compression Ratio Calculation
* 📈 Visualization using Matplotlib
* 🧠 Advanced Compression Algorithms
* 🖥️ GUI-Based Image Compressor
* ☁️ Batch Image Compression

---

## 📸 Sample Output

| Original Image | Compressed Image |
| -------------- | ---------------- |
| lena.jfif      | lena_2.jpg       |

The compressed image contains only **8 grayscale intensity levels**, demonstrating a simple yet effective lossy compression technique.

---

## 🏆 Project Highlights

⭐ Manual Pixel Manipulation

⭐ Image Quantization

⭐ NumPy Array Processing

⭐ Pillow-Based Image Handling

⭐ Fundamental Image Compression Concepts

⭐ Beginner-Friendly Computer Vision Project

---

## 📚 Concepts Covered

* Digital Images
* Pixels and Intensity Levels
* Grayscale Conversion
* Quantization
* Lossy Compression
* NumPy Arrays
* Image Processing with PIL

---

## 👨‍💻 Author

**Aritra Chakraborty**
