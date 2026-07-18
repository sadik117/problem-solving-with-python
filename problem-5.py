# Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.

# For example: Input: heads -> 4 legs -> 12
# Output: dogs -> 2 chicken -> 2

heads = int(input('Enter the number of heads: '))
legs = int(input('Enter the number of legs: '))

# Formula separation for understanding
# heads = dogs + chicken
# dogs = heads - chicken

# legs = 4*dogs + 2*chicken
# legs = 4*(heads - chicken) + 2*chicken

chicken = (4*heads - legs) // 2

dogs = heads - chicken

print('Number of chickenaa: ', chicken)
print('Number of doggy: ', dogs)


# another way to solve using loop
for dogs in range(heads + 1):
    chicken = heads - dogs

    if (4*dogs + 2*chicken) == legs:
        print('Number of doggesh vau: ', dogs)
        print('Number of side chick: ', chicken)
        break
