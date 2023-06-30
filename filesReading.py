lorem_file = open('files/lorem.txt')

for line in lorem_file:
    # print(line)
    print(line.rstrip())

# seek()
lorem_file.seek(0)  # reset the cursor at the start of the text using seek()

# readlines()

lines = lorem_file.readlines()
print(lines)  # this will return us a LIST
# each line in the text will be in the list separated by comma

