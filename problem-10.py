# Problem-1: Write a Python function that takes a list and returns a new list with unique elements of the first list.

# Input:

# [1,2,3,3,3,3,4,5]

# Output:

# [1, 2, 3, 4, 5]


def unique_list(list):
  x = []
  for i in list:
    if i not in x:
      x.append(i)
  return x

print(unique_list([1,2,3,3,3,3,4,5]))