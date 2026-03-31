# 🔢 Number Cycle Analyzer (PyQt5)

A simple PyQt5-based desktop application that explores how numbers transform across **binary, decimal, and hexadecimal systems**, and detects repeating cycles in the process.

---

## 📌 Overview

This application takes a positive integer and repeatedly applies a transformation:

1. Convert the number to binary
2. Reverse the binary representation
3. Convert it back to decimal
4. Add 2
5. Repeat until a cycle is detected

All steps are recorded and displayed in a table.

---

## 🚀 Features

* Accepts any positive integer input
* Tracks number transformations step-by-step
* Displays:

  * Cycle sequence
  * Binary values
  * Hexadecimal values
  * Cycle period
* Detects repeating patterns automatically
* Stores results locally in a file (`amplitude.dat`)

---

## 🖥️ How to Run

### 1. Install dependencies

```
pip install PyQt5
```

### 2. Run the program

```
python project.py
```

> Make sure `interface_project.ui` is in the same folder.

---

## 📁 Files

```
project.py              # Main application logic
interface_project.ui   # GUI layout (Qt Designer)
amplitude.dat          # Generated data file
README.md              # Documentation
```

---

## ⚠️ Notes

* Input must be a **positive integer**
* The program stops if no cycle is found within 1024 iterations
* Results are appended to `amplitude.dat`

---

## 💡 Idea Behind the Project

This project demonstrates how number representations (binary ↔ decimal) can produce interesting repeating behaviors when transformed iteratively.

---

## 👤 Authors

* Abdihafith
* Bilal
