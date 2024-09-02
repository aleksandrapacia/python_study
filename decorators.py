#1. nested functions

def outer(x):
    def inner(y):
        return x+y  
    return inner

add_five = outer(5)
result = add_five(6)
print(result)

#2. passing function as an argument in another function

def add(x,y):
    return x + y

def calculate(func, x, y):
    return func(x,y)

result = calculate(add, 4, 5)
print(result) # prints 9

#3. return function as a value

def greeting(name):
    def hello():
        return "Hello, " + name + "!"
    return hello

greet = greeting("Aleksandra")
print(greet())

#4. using DECORATOR
def make_pretty(func):

    # define the inner function 
    def inner():

        #add some additional behatior to decorated function
        print("I got decorated")

        # call original function
        func()
    
    #return the inner function
    return inner

# def define oridinary function
@make_pretty
def ordinary():
    print("I am ordinary")

# easier way to decorate
ordinary()

#5. decorating functions with parameters
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide ", a, " and ", b)
        if b == 0:
            print("Whoops! I cannot divide!")

        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('Cant divide by 0')

divide(2,5)
divide(2,0)

#6. chaining the decorators
def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner

@star
@percent 
def printer(msg):
    print(msg)

printer("Hello")