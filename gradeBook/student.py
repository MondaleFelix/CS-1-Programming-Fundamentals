class Student():

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignment = {}

        # Iterates through the assignment dictionary and returns the medium of all grades (values)
    def get_gpa(self):
        final = 0
        for i in self.assignment.values():
            final += i
        return final / len(self.assignment)

        # Goes through the dictionary and adds the assignment and grade that is passed through
    def add_assignment(self, assignment, grade):
        self.assignment[assignment] = grade

        # Removes the assignment from the assignment dictionary
    def delete_assignment(self, assignment):
        self.assignment.pop(assignment)

        # removes the assignment and adds one
    def update_assignment(self, assignment, grade):
        delete_assignment(assignment)
        add_assignment(assignment, grade)
        #DRY

    def get_assignment(self):
        return self.assignment
        # returns the dictionary of the assignment and the Grade
