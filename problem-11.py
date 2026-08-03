# Problem 3: Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

# Sample String : 'CampusX is an Online Mentorship Program fOr EnginEering studentS.'
# Expected Output :
# No. of Upper case characters :  9
# No. of Lower case Characters :  47


def calculation(text):
    words = text.split()

    upper_count = 0
    lower_count = 0

    for word in words:
        for char in word:
            if char.isupper():
                upper_count += 1
            elif char.islower():
                lower_count += 1
    return upper_count, lower_count

upper, lower = calculation(
    'CampusX is an Online Mentorship Program fOr EnginEering studentS.'
)

print("No. of Upper case characters :", upper)
print("No. of Lower case Characters :", lower)