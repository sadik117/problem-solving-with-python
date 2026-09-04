# Q: Cast vote
# Write a program that validate name and age as entered by the user to determine whether the person can cast vote or not. To handle the age, create InvalidAge exception and for name, create InvalidName exception. The name will be invalid when the string will be empty or name has only one word.

# Example 1:
# Input:

# Enter the name: goransh singh
# Enter the age: 25

# Output:
# Goransh Singh  Congratulation !!! You can vote.

class InvalidAgeError(Exception):

    def __init__(self, message):
        print(message)

class InvalidNameError(Exception):

    def __init__(self, message):
        print(message)

class Vote:

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def cast_vote(self):
            if self.age <= 18:
                raise InvalidAgeError('Your age is under 18 and you cannot vote')
            
            if len(self.name.split()) < 2:
                raise InvalidNameError('Your name should have been at least two words')
            print(self.name, 'Congratulation!! You can vote.')

obj = Vote(22, 'Sadik')

try:
    obj.cast_vote()
except Exception as e:
    print(e)



