# Inheritance
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def voice(self):
        print("Bark!")

class Cat(Animal):
    def getvoice(self):
        print("Meow!")

dog = Dog("Burek", 5)
print(dog.name)
print(dog.age)
dog.voice()

class Wolf(Dog):
    def returnVoice(self):
        super().voice()

wolf = Wolf("Geralt", 50)
wolf.returnVoice()
cat = Cat("Mruczek", 3)
print(cat.name)
print(cat.getvoice())