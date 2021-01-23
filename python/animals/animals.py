class Animal:
    def __init__(self, name):
        self.name = name

    def whoami(self):
        return self.name

    def speak(self):
        print("The animal refuses to speak")


class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)

    def speak(self):
        print("Meow!")


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)

    def speak(self):
        print("Woof!")


class Fish(Animal):
    def __init__(self, name):
        super(Fish, self).__init__(name)
