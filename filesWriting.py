with open('files/write.txt', 'w') as write_file:
    write_file.write('Hello world this is me')
    write_file.write('\nI am planning to teach python later')



# amend to a file

with open('files/write.txt', 'a') as write_file:
    write_file.write('\nHello world this is me again')


quotes = [
    '\nSomething in the rain',
    '\nWhen it\'s night I watch',
    '\nWhat to do, you asked...'
]


with open('files/write.txt', 'a') as write_file:
    write_file.writelines(quotes)


