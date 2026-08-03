# Problem 4: Write a Python program to print the even numbers from a given list.

# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

def even_number(list):
    even_numbers_list = []
    for num in list:
        if num % 2 == 0:
            even_numbers_list.append(num)

    return even_numbers_list

print(even_number([1, 2, 3, 4, 5, 6, 7, 8, 9]))