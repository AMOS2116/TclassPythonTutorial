# function is a block of code that only runs when it is called. in python we use identation and not curly brackets

# Returns value

def addNum(num1, num2):
    total = num1 + num2
    return total


def subNum(num1, num2):
    difference = num1 - num2
    return difference

print(addNum(20, 8))
print(subNum(80, 30))

# Create function
def sayHelloWorld(name='abdul'):
    print(f'Hello {name}')

print(sayHelloWorld('casmir'))

# A lambda function is a small anonymous function. it can take any number 
#of arguments , but can only have one expression. very similar to the javascript arrow function

addNum = lambda num1, num2: num1 + num2

print(addNum(30, 40))