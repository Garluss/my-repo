import matplotlib.pyplot as plt

class School():
    def __init__(self,size):
        self.size = size
        self.size_remaining = size
        self.students = []
        self.teachers = []
    def new_student(self,student):
        if self.size_remaining <= 0:
            return
        self.size_remaining -= 1
        self.students.append(student)
    def new_teacher(self,teacher):
        self.teachers.append(teacher)
    def remove_student(self,student):
        if student in self.students:
            self.students.remove(student)
    def get_students(self):
        list = []
        for i in self.students:
            list.append(i.name)
        return list
    def get_personell(self):
        return self.teachers
    def get_spaces(self):
        return self.size_remaining

class Student():
    def __init__(self,name,grade,satisfaction,grades):
        self.name = name
        self.grade = grade
        self.satisfaction = satisfaction
        self.grades = grades
    def get_grades(self):
        return self.grades

class Teacher(Student):
    def __init__(self,name,satisfaction,subject):
        super().__init__(name,None,satisfaction,None)
        self.subject = subject

nick = Student("Nick Gomez",2,67,{"math":6,"IT":2})
braden = Student("Braden N.",4,34,{"math":2})

brown = Teacher("Mr. Brown",78,["math","physics"])

AsVs = School(10)

AsVs.new_student(nick)
print(AsVs.get_students())
AsVs.remove_student(nick)
print(AsVs.get_students())
print(nick.get_grades())