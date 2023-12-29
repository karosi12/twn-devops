from person import Person

class Student(Person):

    def __init__(self, first_name, last_name, age, lectures=None):
        super().__init__(first_name, last_name, age)
        if lectures is None:
            self.lectures = []
        else:
            self.lectures = lectures

    def lecture_list(self):
        return self.lectures
    
    def add_lecture(self, lecture):
        if lecture not in self.lectures:
            self.lectures.append(lecture)
        return self.lectures

    def remove_lecture(self, lecture):
        if lecture in self.lectures:
            self.lectures.remove(lecture)
        return self.lectures