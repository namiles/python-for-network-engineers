"""
Python is a dynamically typed language - meaning you do not have to specify an objects typ such as int, float, string, etc.

This can sometimes cause issues, especially if another developer is using your code but does not know what functions accept what types, or what they return.

Typing can be used to "hint" at what type an object is or should be. It HAS NO AFFECT on the code and act more like annotations.
Type hints are not required.
Most IDEs can use type hints within the development environment to make writing code easier.
"""

# We can use type hints to hint at what type an argument should be, and what type a function returns.
# In the say_hello function, we accept an string argument and return a string object.
def say_hello(name: str) -> str:
    return f"Hello, {name}"


def main():
    x = "Network"  # Dynamically creates a str object
    y = 3  # Dynamically creates an int object

    # In a statically typed language, the above would look something like:
    # str x = "network"
    # int y = "3"

    print(type(x))
    print(type(y))

    name = input("\nEnter your name: ")

    # If using an IDE - By moving the mouse cursor over the say_hello() function call here, you should be able to see 
    # that name should be a string and the function returns a string.
    print(say_hello(name))


if __name__ == "__main__":
    main()
