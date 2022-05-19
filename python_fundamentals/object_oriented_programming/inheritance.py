"""
Inhertience applies to objects with a Is-A relationship.

For example, a French Bulldog IS A Dog.
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sounds(self):
        return "Woof"


class FrenchBulldog(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def breathing(self):
        return "Gremlin"

    # Ovveride a method from the parent object
    # This method ovverrides the parent method because it is more specific to the derived class
    def sounds(self):
        return "wooooooooof"

def main():
    my_dog = FrenchBulldog("murphy", "2")
    print(my_dog.name)
    print(my_dog.age)
    print(my_dog.sounds())


if __name__ == "__main__":
    main()
