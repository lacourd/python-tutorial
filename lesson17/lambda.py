#  A single, anonymous function that returns a value

squared = lambda num : num * num

print(squared(2))

addTwo = lambda num : num + 2

print(addTwo(12))

sum_total = lambda a, b : a + b

print(sum_total(43, 64))



###########################
# Lambdas are used for quick functions inside of other functions

def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

###########################

# Higher order functions:
# function that takes functions as its argument(s) OR that returns a function as its result

# map takes a function as its first parameter, followed by a collection, and then applies the function to each item in the collection

numbers = [3,7,12,18,20,21]

squared_nums = map(lambda num : num * num, numbers)

print(list(squared_nums))

#########################

# filter takes a function as its first parameter, followed by a collection, and then evaluates each item in the collection with respect to the function, returning a new collection with only True values.

odd_nums = filter(lambda num : num % 2 != 0, numbers)

print(list(odd_nums))

##########################

from functools import reduce



numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

print(sum(numbers))




names = ["Dave Gray", "Sara Ito", "John Jacob Jingleheimerschmidt"]

char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)

print(char_count)