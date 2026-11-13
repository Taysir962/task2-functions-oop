
class Student:
    """A class representing a Student with name and grades list."""
    
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, g):
        """Adds a grade if it's between 0 and 100, otherwise raises ValueError."""
        if not (0 <= g <= 100):
            raise ValueError("Grade must be from 0 to 100.")
        self.grades.append(g)

    def average(self):
        """Returns the average of grades, or 0 if no grades exist."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Student({self.name}, Average: {self.average():.2f})"


class Course:
    """A class representing a Course containing multiple students."""
    
    def __init__(self, title):
        self.title = title
        self.students = []

    def add_student(self, student):
        """Adds a student object to the course."""
        self.students.append(student)

    def class_average(self):
        """Returns the overall average of all students in the course, or None if no students."""
        if not self.students:
            return None
        total_avgs = [s.average() for s in self.students]
        return sum(total_avgs) / len(total_avgs)

    def top_student(self):
        """Returns the student with the highest average, or None if no students."""
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.average())

    def __str__(self):
        return f"Course: {self.title} ({len(self.students)} students)"


if __name__ == "__main__":
    print("=== Testing Student and Course Classes ===")
    
    course = Course("Python Programming")
    
    s1 = Student("Ali")
    s1.add_grade(85)
    s1.add_grade(90)
    
    s2 = Student("Sara")
    s2.add_grade(95)
    s2.add_grade(100)
    
    course.add_student(s1)
    course.add_student(s2)
    
    print(course)
    print("Class Average:", course.class_average())
    print("Top Student:", course.top_student().name)
    
    print("-" * 30)

    try:
        s1.add_grade(150)  # درجة غير صالحة (> 100)
    except ValueError as e:
        print("Caught expected ValueError:", e)