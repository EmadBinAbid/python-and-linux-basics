"""
Write a python3 program that defines an Animal base class and three derived classes that inherit from Animal: Cat,
Dog, and Fish classes.

The Animal base class should take the animal’s name (such as “rover”) as an argument to its constructor. The Animal
class should have a method “whoami” that returns the name value to the caller. The animal class should have an
implementation of the “speak” method that prints out “The animal refuses to speak”—this will be a default method
incase no derived class implements it.

Three derived classes (Cat, Dog, and Fish) should take name as their constructor argument and in turn pass it to the
Animal base class constructor. Extra credit for utilizing python 3.1’s new enhanced super() function to avoid hard
coding the base class name. The Cat class should implement a “speak” method that prints “Meow!”. The Dog class should
implement a “speak” method that prints “Woof!”. The Fish class should not implement a “speak” method, as fish do not
speak.

Once the base class and three derived classes are written, create a mainline program/script (in the same file) that
creates an empty list named “animals” and then appends a Dog named “Rover”, a Cat named “Hank”, and a Fish named “Fred”
to the list. After the list is populated with the three derived Animal instances, iterate the list and for each animal,
print the animal’s name and then call it’s speak method.
"""

from python.animals.animals import Cat, Dog, Fish


def main():
    animals = list()

    animals.append(Dog("Rover"))
    animals.append(Cat("Hank"))
    animals.append(Fish("Fred"))

    for animal in animals:
        print("This animal's name is " + animal.name)
        animal.speak()


if __name__ == '__main__':
    main()
