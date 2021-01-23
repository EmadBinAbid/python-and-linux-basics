def meow():
    print("Meow!")


def bark():
    print("Woof!")


class Animal:
    def speak(self):
        raise Exception("Unknown object found!")


class Cat(Animal):
    def speak(self):
        meow()


class Dog(Animal):
    def speak(self):
        bark()


def type_troubles(obj):
    obj.speak()
