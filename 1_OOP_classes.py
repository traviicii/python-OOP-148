from helper import d
# Object Oriented Programming and Classes

# OOP: a concept revolving around "blueprints" (classes) that help us to create multiple objects with similar attributes and behaviors

# Why use this OOP concept?

#-- Modularity: OOP allows for better organizations of code by breaking it down into (reuseable) pieces (classes and objects)
#-- Reuseability: Once we build a class, we can reuse it to create multiple objects, reducing redundancy
#-- Scalability: Reusing code allows us to scale our applications with more efficency
#-- Maintenance: OOP makes it easier to update specific instances of an object rather than modifying an entire catalog of data, or an entire codebase

# what are classes and objects?

#-- Classes: the blueprint that outlines the attributes and functionality of an object.
#-- Object: A unique instance of a class, created based on the blueprint (class)

# We've been working with classes and objects this entire time!!!
num = 2
str1 = str()
print(type(str1))

list1 = list()
print(type(list1))

dictionary_1 = dict()
print(type(dictionary_1))

# Let's create our own class
# Naming Convention for user defined classes: always capitalize the first letter
class Car():
    pass

# def my_func():
#     pass

d()

my_car = Car()
print(type(my_car))

bugati = Car()
my_other_car = Car()

