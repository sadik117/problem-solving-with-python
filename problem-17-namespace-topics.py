# Q1: Write Person Class as given below and then display it's namespace.

# Class Name - Person

# Attributes:
# name - public
# state - public
# city - private
# age - private

# Methods:
# address - public
# It give address of the person as "<name>, <city>, <state>"

# And also write a program to show namespace of object/instance of above(Person) class.



class Person:

    def __init__(self, name, state, city, age):
        self.name = name
        self.state = state
        self.__city = city
        self.__age = age

    def address(self):
        return f"{self.name}, {self.__city}, {self.state}"


p1 = Person('Sadik', 'Bangladesh', 'Rajshahi', 22)

print(p1.address())

print(Person.__dict__)