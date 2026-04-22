#TASK 1

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = int(marks)

    def show_grade(self):
        if self.marks >= 80:
            print(self.name, "got Grade A ")
        elif self.marks >= 60:
            print(self.name, "got Grade B ")
        else:
            print(self.name, "got Grade C ")

s1 = Student("Mudasir","45")
s2 = Student("Yousuf","67")
s3 = Student("Ali","87")
s4 = Student("Zeeshan","64")

s1.show_grade()
s2.show_grade()
s3.show_grade()
s4.show_grade()