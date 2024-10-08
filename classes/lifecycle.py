class Test:


    def __del__(self):
        print('Goodbye Class')

obj = Test()
obj2 = obj
lista = [obj2]
del obj
del obj2
del lista[0]
# init -> constructor
# del -> destructor
print("The end")