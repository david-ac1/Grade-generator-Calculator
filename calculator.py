# calculator.py

def categorize_assignments(assignments):
    formative = []
    summative = []
    # Categorize each assignment based on its type
    # Assuming each assignment has a 'category' attribute
    for a in assignments:
        if a.category == 'Formative':
            formative.append(a)
        elif a.category == 'Summative':
            summative.append(a)
    return formative, summative

def get_total_weight(assignments):
    # Sum weights of all assignments in a category
    return sum(a.weight for a in assignments)

def get_total_weighted_grade(assignments):
    # Sum weighted grades of assignments in a category
    return sum(a.get_weighted_grade() for a in assignments)

def calculate_gpa(overall_weighted_grade, total_weight):
    # Normalize GPA to 5 based on total weight
    if total_weight == 0:
        return 0  # Avoids dividing by zero
    return (overall_weighted_grade / total_weight) * 5

def determine_pass_fail(formative_score, summative_score, formative_weight, summative_weight, average_threshold=50):
    """
    Determines pass/fail status by normalizing the category scores.
    - Pass if both normalized scores are >= average threshold (default = 50%).
    - Fail if either or both are below.
    """
    if formative_weight == 0 or summative_weight == 0:
        return "Fail and Repeat"  # Not enough data

    # Normalize both scores to percentage
    formative_percent = (formative_score / formative_weight) * 100
    summative_percent = (summative_score / summative_weight) * 100

    if formative_percent >= average_threshold and summative_percent >= average_threshold:
        return "Pass"
    else:
        return "Fail and Repeat"
