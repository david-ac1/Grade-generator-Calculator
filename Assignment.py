class Assignment:
    def __init__(self, name, category, weight, grade):
        #student name
        self.name = name
        #formative or summative
        self.category = category
        #Grade class achievable
        self.weight = weight
        #Grade class achieved
        self.grade = grade

    def get_weighted_grade(self):
        #Returns the weighted grade for the assignment
        return (self.weight * self.grade) / 100
    
    def __str__(self):
        #Returns a string representation of the assignment
        return f"Assignment(name={self.name}, category={self.category,}, weight={self.weight}%, grade={self.grade})"