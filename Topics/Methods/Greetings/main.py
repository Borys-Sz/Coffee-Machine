class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, I am {}!".format(self.name))


person = Person(input())
person.greet()