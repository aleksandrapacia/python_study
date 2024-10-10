class Test:
    # _lista is a private variable
    # __lista is a protected variable
    __lista =  []
    def dodaj(self, arg):
        self.__lista.append(arg)

    def zdejmij(self):
        if len(self.__lista) > 0:
            return self.__lista.pop(len(self.__lista)-1)
        else:
            return

obj = Test()
obj.dodaj("a")
obj.dodaj("b")
print(obj.zdejmij())
print(obj.zdejmij())
obj._Test__lista.append("X")
print(obj._Test__lista)
