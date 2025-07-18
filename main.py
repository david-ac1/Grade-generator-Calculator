# main.py
from input_handler import get_assignment_input

def main():
    assignments = []

    num = int(input("How many assignments do you want to enter? "))
    for _ in range(num):
        assignment = get_assignment_input()
        assignments.append(assignment)

    print("\nAll Assignments Entered:")
    for a in assignments:
        print(a)

if __name__ == "__main__":
    main()
