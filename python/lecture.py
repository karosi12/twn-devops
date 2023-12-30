class Lecture():

    def __init__(self,  name, max_num_of_students, duration, professors):
        self.name = name
        self.max_num_of_students = max_num_of_students
        self.duration = duration
        self.professors = professors

    def professor_list(self):
        return self.professors
    
    def lecture_duration(self):
        return self.name +" "+ self.duration
    
    def add_professor(self, professors):
        return self.professors + professors
