# Q: 

# Statement: A university wants to automate their admission process. Students are admitted based on the marks scored in the qualifying exam. A student is identified by student id, age and marks in qualifying exam. Data are valid, if:
#     Age is greater than 20
#     Marks is between 0 and 100 (both inclusive)

# A student qualifies for admission, if
#     Age and marks are valid and
#     Marks is 65 or more

# Write a python program to represent the students seeking admission in the university. Also use getter and setter method to get and set the values of the instances.


class Student:

    def __init__(self, student_id, marks, age):

        self.__student_id = student_id
        self.__marks = marks
        self.__age = age

    def get_student_id(self):
        return self.__student_id

    def set_student_id(self, new_id):
        if type(new_id) == int:
            self.__student_id = new_id
        else:
            print('Student id should be numeric')

    def get_marks(self):
        return self.__marks

    def set_marks(self, new_marks):
        if type(new_marks) == int:
            self.__marks = new_marks
        else:
            print('Marks should be integer')

    def validate_marks(self, marks):
        if 0 <= marks <= 100:
            return True
    def validate_age(self, age):
        if age > 20:
            return True

    def check_qualification(self):
        if self.validate_marks(self.__marks) and self.validate_age(self.__age) and self.__marks >= 65:
            print('Student is qualified for admission')
        else:
            print('Student is not qualified')

stud1 = Student(2112, 65, 21)
stud1.check_qualification()
stud1.set_student_id(1003)
print(stud1.get_student_id())
stud1.set_marks(69)
print(stud1.get_marks())

        