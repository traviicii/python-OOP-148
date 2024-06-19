from helper import d
# Creating Attributes for our classes

# What's an attribute?
#-- Attributes define the qualities of our objects and are stored in variables within a class

# two different types of attributes

#-- Class Attributes: Attributes that are shared between all instances of a class
#-- Instance Attributes: Attributes that can vary between different instances of a class

class Car():
    # class attribute example
    wheels = 4

    def __init__(self, make, model):
        # Instance attributes
        self.make = make
        self.model = model

# Create a few instances of the car class
bugati = Car("Bugati", "Veyron")
tesla = Car('Tesla', "Model S")

print("BUGATI")
print(bugati.wheels)
print(bugati.model)

d()

print("TESLA")
print(tesla.wheels)
print(tesla.model)

list1 = []
list1.append(1)

d()

# Class Methods

#-- Methods define the actions or functionalities that our objects can perform. 
x = "Some kinda stuff" # quick global variable test

class Car():
    def __init__(self, make, model, mileage= 0): # __init__ method must always contain self as the first parameter
        self.make = make
        self.model = model
        self.mileage = mileage

    # Method to get car info
    def get_info(self):
        # print(x) # accessing a global variable
        print(f"This is a {self.make} {self.model}!")

    # Method to drive the car
    def drive(self, miles):
        self.mileage += miles
        print(f"This {self.make} drove {miles} miles. Now the total mileage is {self.mileage}")


tesla = Car("Tesla", "Model S", mileage= 312)
tesla.get_info()

bugati = Car("Bugati", "Veyron")
bugati.get_info()

tesla.drive(253)
bugati.drive(75)