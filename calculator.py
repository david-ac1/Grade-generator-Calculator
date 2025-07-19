# calculator.py

def categorize_assignments(assignments):
    formative = []
    summative = []
    #We use a for loop to categorize assignments into formative and summative
    for a in assignments:
        if a.category == 'Formative':
            formative.append(a)
        elif a.category == 'Summative':
            summative.append(a)
    return formative, summative

def get_total_weight(assignments):
    return sum(a.weight for a in assignments)

def get_total_weighted_grade(assignments):
    return sum(a.get_weighted_grade() for a in assignments)

def calculate_gpa(overall_weighted_grade):
    # Convert total score (out of 100) to GPA (out of 5)
    return (overall_weighted_grade / 100) * 5

def determine_pass_fail(formative_score, summative_score, average_threshold=50):
    """
    Determines pass/fail status.
    - Pass if both scores ≥ average threshold.
    - Fail and Repeat otherwise.
    """
    if formative_score >= average_threshold and summative_score >= average_threshold:
        return "Pass"
    else:
        return "Fail and Repeat"
