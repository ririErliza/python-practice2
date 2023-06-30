lorem_file = open('files/lorem.txt')

for line in lorem_file:
    # print(line)
    print(line.rstrip())


# readlines()

lines = lorem_file.readlines()
print(lines)  # this will return us a LIST