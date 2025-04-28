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
        return self.students
    def get_personell(self):
        return self.teachers
    def get_spaces(self):
        return self.size_remaining

class Student():
    def __init__(self,name,grade,satisfaction):
        self.name = name
        self.grade = grade
        self.satisfaction = satisfaction

class Teacher(Student):
    def __init__(self,name,satisfaction,subject):
        super().__init__(name,None,satisfaction)
        self.subject = subject

nick = Student("Nick Gomez",2,67)
braden = Student("Braden N.",4,34)

brown = Teacher("Mr. Brown",78,"math")

AsVs = School(10)

AsVs.new_student(nick)
print(AsVs.get_students())
AsVs.remove_student(nick)
print(AsVs.get_students())