from input_handler import get_assignment_input
from calculator import (
    categorize_assignments,
    get_total_weight,
    get_total_weighted_grade,
    calculate_gpa,
    determine_pass_fail
)

def main():
    assignments = []

    num = int(input("Oya, How many assignments do you want to enter? "))
    for _ in range(num):
        assignment = get_assignment_input()
        assignments.append(assignment)

    # Categorize assignments based on their type
    formative, summative = categorize_assignments(assignments)

    # Calculate category weights
    formative_weight = get_total_weight(formative)
    summative_weight = get_total_weight(summative)
    total_weight = formative_weight + summative_weight

    # Calculate weighted scores
    formative_score = get_total_weighted_grade(formative)
    summative_score = get_total_weighted_grade(summative)
    overall_score = formative_score + summative_score

    # Normalize GPA based on total weight
    if total_weight > 0:
        gpa = (overall_score / total_weight) * 5
    else:
        gpa = 0  # Then no assignments entered

    # Result: Pass or Fail
    decision = determine_pass_fail(
        formative_score,
        summative_score,
        formative_weight,
        summative_weight
    )

    # Output Summary
    print("\n Grade Summary:")
    print(f"Formative Total: {formative_score:.2f} (Weight: {formative_weight}%)")
    print(f"Summative Total: {summative_score:.2f} (Weight: {summative_weight}%)")
    print(f"Total Weighted Score: {overall_score:.2f} (Total Weight: {total_weight}%)")
    print(f"GPA (out of 5): {gpa:.3f}")
    print(f"Result: {decision}")

    # Warnings
    if total_weight < 100:
        print(f"\n Warning: You've only entered {total_weight}% of the course grade. GPA is based on partial data.")
    elif total_weight > 100:
        print(f"\n Error: Total course weight exceeds 100% ({total_weight}%). Please check your inputs.")

if __name__ == "__main__":
    main()
