class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32
    
    # getter method 
    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature
    
    @temperature.setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._temperature = value
    

"""instead of it ...     
# creating a new object
human = Celsius(37)

# get the temperature attribute via a getter
print(human.get_temperature())

# get the to_fahrenheit method , get_temperature
#called by the method itself
print(human.to_fahrenheit())

# new constraint imprementation 
human.set_temperature(-300)

# het the to_fahrenheit method
print(human.to_fahrenheit)
"""
#use this:
# create a property object (line 18)

human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

coldest_thing = Celsius(-300)