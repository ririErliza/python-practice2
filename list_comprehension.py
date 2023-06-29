# List Comprehensions

# List comprehension offers a shorter syntax when you 
# want to create a new list based on the values of an 
# existing list.

prizes = [50, 100, 500, 1000]

# an example, we want to create a new list that double
# the existing prizes

dbl_prizes = []

for prize in prizes:
    dbl_prizes.append(prize*2)

print(dbl_prizes)
# [100, 200, 1000, 2000]

# comprehension method
dbl_prizes_prizes = [prize*2 for prize in prizes]
print(dbl_prizes)
# [100, 200, 1000, 2000]



# squaring numbers
nums = [1,2,3,1,2,3,1,2,3]

squared_even_nums = []
for num in nums:
    if(num**2)%2 ==0:
        squared_even_nums.append(num**2)

print(squared_even_nums)
# [4, 4, 4]

# comprehension method
squared_even_nums = [num**2 for num in nums if (num**2)%2==0]
print(squared_even_nums)
# [4, 4, 4]
