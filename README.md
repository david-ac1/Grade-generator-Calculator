# 📘 Grade Generator Calculator: Individual Coding Lab

A Python application built as part of **ALU BSE Year 1 Trimester 2 Lab 1**. This tool helps students understand how their assignment grades contribute to their overall course grade. It supports both formative and summative assessments, calculates the GPA, and determines whether the student passes or must repeat the course.

---

## ✅ Features

- 🚀 Interactive user input for assignments
- 🗂️ Categorizes assignments into **Formative** or **Summative**
- 📊 Applies weightings to calculate each assignment's contribution
- 🎓 Computes GPA out of 5 based on total weighted score
- 📉 Determines **Pass** or **Fail and Repeat** status based on category-wise performance
- 🛡️ Validates input data (grade range, weight limits, etc.)
- 🔍 Gives warnings for incomplete or overweighted grade entries

---

## 📂 File Structure

```bash
grade_calculator/
├── main.py               # Main program that runs the application
├── Assignment.py         # Defines the Assignment class
├── input_handler.py      # Handles user input and validation
├── calculator.py         # Contains calculation logic (GPA, totals, decision)
└── README.md             # This file

```
## 🧪 How to Run
- Make sure you have Python 3.x installed.

- Open a terminal in the project folder.

- Run the program: python main.py

## ⚠️ Notes & Validations

- Grade must be a number between 0 and 100

- Weight must be a number between 0 and 100

- Total weights across all assignments should ideally sum to 100%

- If weights are incomplete or exceed 100%, a warning is shown

## Developed By David Achibiri
## African Leadership University