name = "Mark"     #global variable
def naming_func(name):
    print(f'Hello, {name},')
naming_func(name)

def age():      
    age = 23      #local variable
    print(f'You are {age} years old!')
age()