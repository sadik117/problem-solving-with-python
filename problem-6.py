# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# Given List:

# list1 = ["M", "na", "i", "Kh"]
# list2 = ["y", "me", "s", "an"]

# Output:

# [['M','y'], ['na', me'], ['i', 's'], ['Kh', 'an']]


list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]

result = []

for i in range(len(list1)):
    pair = list1[i], list2[i]
    result.append(pair)

print(result)


# Another way to solve using zip and list comprehensive function

list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]

print([[i,j] for i,j in zip(list1,list2)])



# Another tricky solve to concate the strings

list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]

print([i+j for i,j in zip(list1, list2)])

# output: ['My', 'name', 'is', 'Khan']