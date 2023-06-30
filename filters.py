# filters

# filter(testing_function, data collection)

grades = ['A', 'B', 'B', 'C', 'F', 'A', 'F']


# we want to filter the list above
# and get a NEW list with no F

def remove_fails(grade):
    return grade != 'F'

newGrades = list(filter(remove_fails,grades))
print(newGrades)
# ['A', 'B', 'B', 'C', 'A']

print(grades)
# ['A', 'B', 'B', 'C', 'F', 'A', 'F']



# -------------------------------------------------

# using for loop

filtered_grades = []
for grade in grades :
    if grade != 'F':
        filtered_grades.append(grade)

print(filtered_grades)
# ['A', 'B', 'B', 'C', 'A']

# -------------------------------------------------

# using comprehension

print([grade for grade in grades if grade != 'F'])
# ['A', 'B', 'B', 'C', 'A']


