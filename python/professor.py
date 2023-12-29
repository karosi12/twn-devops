from person import Person

class Professor(Person):

    def __init__(self,first_name, last_name, age, subjects=None):
        super().__init__(first_name, last_name, age)
        if subjects is None:
            self.subjects = []
        else:
            self.subjects = subjects

    def subject_list(self):
        return self.subjects
    
    def add_subject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)
        return self.subjects

    def remove_subject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)
        return self.subjects