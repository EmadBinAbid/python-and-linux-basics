"""
Implement a python3 function that accepts one argument named “pet”, but acts differently based on the type of object
passed in. If the function is passed a Dog object, call the bark() method on the object. If the function is passed a
Cat object, call the meow() method on the object. If neither a Dog or Cat is passed, raise an exception.
"""

from python.type_troubles.type_troubles import type_troubles, Cat, Dog


def main():
    cat = Cat()
    dog = Dog()

    type_troubles(cat)
    type_troubles(dog)


if __name__ == '__main__':
    main()
