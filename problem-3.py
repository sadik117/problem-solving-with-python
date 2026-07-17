# Problem 13:Print all the Armstrong numbers in a given range.
# Range will be provided by the user
# Armstrong number is a number that is equal to the sum of cubes of its digits. 
# For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.

start_num = int(input('Enter your starting number: '))
end_num = int(input('Enter your end number: '))

for number in range(start_num, end_num + 1):
    armstrong_num = number
    total = 0

    while number > 0:       
        digit = number % 10
        total = total + (digit ** 3)

        number = number // 10

    if total == armstrong_num:
        print(armstrong_num)