class Student:

    def __init__(self, name, major, gpa, is_active):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_active = is_active

    def print(self):
        print(self.name)
        print(self.major)
        print(self.gpa)
        print(self.is_active)

