from student import Student

# THIS IS THE CLASSROOM OBJECT
class Classroom():
    assignment = None

    def __init__(self, class_name,):
        self.class_name = class_name
        self.roster = {}
        self.student_assignments = []
        self.student_grades = {}

    def get_gpa():
        final = 0
        for i in self.assignment.values():
            final += i
        return final / len(self.roster)

        # This function adds assignments
    def add_assignment(self, assignment, student_id, grade):
        self.roster[student_id].add_assignment(assignment, grade)

        # This function adds a student
    def add_student(self, student):
        self.roster[student.student_id] = student

        # This function deletes a student
    def remove_student(self, student):
        self.roster.pop(student)

        # This function deletes an assignment
    def delete_assignment(self, student, assignment):
        student.delete_assignment(assignment)
