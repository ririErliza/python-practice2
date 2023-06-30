# lambdas


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, 
# but can only have one expression.

x = lambda a : a + 10
print(x(5))
# 15

x = lambda a, b : a * b
print(x(5, 6))
# 30

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
# 13


# The power of lambda is better shown when you use them 
# as an anonymous function inside another function.

# Say you have a function definition that takes one 
# argument, and that argument  will be multiplied with 
# an unknown number:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))



# a bit like an anonymous function
# it doesnt need a name
# if we only going to use a function once
# there is no need to name it


nums = [1,2,3,4,5,6,7]

# here we use def function to map a list and give a new list

def square(n):
    return n*n

print(list(map(square,nums)))
# [1, 4, 9, 16, 25, 36, 49]


# we can use LAMBDA instead of writing the code as above

print(list(map(lambda n:n*n, nums)))
# [1, 4, 9, 16, 25, 36, 49]