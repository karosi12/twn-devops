from professor import Professor

class Lecture(Professor):

    def __init__(self, first_name, last_name, age, name, max_num_of_students, duration, professors,subjects=None):
        super().__init__(first_name, last_name, age, subjects)
        self.name = name
        self.max_num_of_students = max_num_of_students
        self.duration = duration
        self.professors = professors

    def professor_list(self):
        return self.professors
    
    def lecture_durations(self):
        return self.name +" "+ self.duration
    
    def add_professor(self, names):
        return self.professors + names
