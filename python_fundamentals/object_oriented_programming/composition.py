"""
Composition applies to objects that have a HAS A relationship.

For example, a car HAS A engine.
"""


class Engine:
    def __init__(self, cylinders):
        self.cylinders = cylinders

    def engine_info(self):
        info = f"Cylinders:       {self.cylinders}\n"
        return info


class Car:
    def __init__(self, make, model, color, cylinders):
        self.make = make
        self.model = model
        self.color = color
        self.engine = Engine(cylinders=cylinders)

    def engine_info(self):
        return self.engine.engine_info()


def main():
    my_car = Car("Nissan", "Altima", "Silver", "6")
    print(my_car.engine_info())


if __name__ == "__main__":
    main()
