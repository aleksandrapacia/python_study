x = 12
y = 2
#1.
try:
    lista = [1,2,3]
    print(lista[0])
    # try block - code that may raise an exception
    print(x + 4)
    print( x / y)
    print('Line after')
    # concrete exception
except (ZeroDivisionError, TypeError):
    # except block - code that will be executed if an exception is raised
    print("Error - you can't divide by zero")
    print("1. Cannot add int to string")
# all the other exception
except:
    print("Different error")

finally:
    print('FINALLY: ill do it anyway')
print('Further instructions...')

#2.
try:
    print(x + "!")
except TypeError:
    print('2. Cannot add int to string')