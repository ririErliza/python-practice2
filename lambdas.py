# lambdas
# a bit like an anonymous function
# it doesnt need a name
# if we only going to use a function once
# there is no need to name it
# so we can just use lambda
# say like when we map a list or filter a list

# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, 
# but can only have one expression.

nums = [1,2,3,4,5,6,7]

# here we use def function to map a list and give a new list

def square(n):
    return n*n

print(list(map(square,nums)))
# [1, 4, 9, 16, 25, 36, 49]


# we can use LAMBDA instead of writing the code as above

print(list(map(lambda n:n*n, nums)))
# [1, 4, 9, 16, 25, 36, 49]