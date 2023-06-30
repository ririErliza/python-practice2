# lorem_file = open('files/lorem.txt')

# for line in lorem_file:
#     # print(line)
#     print(line.rstrip())

# # seek()
# lorem_file.seek(0)  # reset the cursor at the start of the text using seek()

# # readlines()

# lines = lorem_file.readlines()
# print(lines)  # this will return us a LIST
# # each line in the text will be in the list separated by comma

# lorem_file.close()

# #---------------------------------------------
# lorem_file = open('files/lorem.txt')
# # getting 100 characters from the 50th character
# lorem_file.seek(50)
# file_text=lorem_file.read(100)
# print(file_text)

# lorem_file.close()

#---------------------------------------------

with open('files/dna_sequence.txt')as dna_file:
    lines = dna_file.readlines()
    print(list(lines))


# #OR
# # if we need to clean up the text a little
# # we can pass a function

# def sequence_filter(line):
#     return'>' not in line

# with open('files/dna_sequence.txt')as dna_file:
#     lines = dna_file.readlines()
#     print(list(filter(sequence_filter, lines)))

