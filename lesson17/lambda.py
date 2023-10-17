#  A single, anonymous function that returns a value

squared = lambda num : num * num

print(squared(2))

addTwo = lambda num : num + 2

print(addTwo(12))

sum = lambda a, b : a + b

print(sum(43, 64))



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