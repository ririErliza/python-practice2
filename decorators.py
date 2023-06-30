# decorators

# A decorator is a design pattern in Python that allows 
# a user to add new functionality to an existing object 
# without modifying its structure. Decorators are usually 
# called before the definition of a function you want to 
# decorate.

def cough_deco(func):
    def func_wrapper():
        #code before function
        print('*cough*')

        func()

        #code after function
        print('*cough*')

    return func_wrapper

@cough_deco
def question():
    print("can you give me discount on that?")

question()

@cough_deco
def answer():
    print("it's just 50p you cheapskate")

answer()


# *cough*
# can you give me discount on that?
# *cough*
# *cough*
# it's just 50p you cheapskate
# *cough*