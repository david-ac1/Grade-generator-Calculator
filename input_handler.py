# input_handler.py
from Assignment import Assignment

def get_assignment_input():
    print("\nEnter assignment details:")

    name = input("Assignment name: ").strip()

    while True:
        category = input("Category (Formative or Summative): ").strip().capitalize()
        if category in ['Formative', 'Summative']:
            break
        else:
            print("Invalid category. Please enter 'Formative' or 'Summative'.")

    while True:
        try:
            grade = float(input("Grade (0-100): "))
            if 0 <= grade <= 100:
                break
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number for grade.")

    while True:
        try:
            weight = float(input("Weight (% of total grade): "))
            if 0 <= weight <= 100:
                break
            else:
                print("Weight must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number for weight.")

    return Assignment(name, category, weight, grade)
