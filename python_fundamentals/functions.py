"""
Functions are constructs in programming that allows code to be broken up into functional pieces.
This helps maintain code reusability and modularity.

In Python, Functions can be a few things:
- Built-in --> Functions that are built into python
- 3rd Party --> Functions proivded by 3rd party libraries/modules
- Customer --> Functions a developer can define and use

** All functions in Python must return something **

Syntax
- Must not start with a number
- Must not be a reserved python word such as print, input, type, etc.
- Can be any combination of letters, numbers, underscores, or dashes.
- Create with the "def" keyword (Ex: def get_hostname(): )


PEP8 Styling for Functions
- Lowercase with words separated by underscores (Ex: retrieve_device_statistics())
- Use one leading underscore for non-public methods and instance variables (Ex: _get_devices())

"""

# Create the function
def my_function():
    """
    Prints "hello, this is my_function()" --> docstring
    """
    print("Hello, this is my_function()")


def my_addition(arg1, arg2):
    sum = arg1 + arg2
    return sum  # pass an arugment back to code that calls function


def my_subtraction(arg1, arg2):
    result = arg1 - arg2
    return result


"""
Unknown amount of arguments
Functions can use * or ** (*args or *kwargs) to defiine a number of arguments or keyword arguments
"""
def say_hello(*args):
    for arg in args:
        print("hello ", arg, "!", sep="")


def main():
    # Call the function
    my_function()

    print(my_addition(5, 5))

    # Keyword Arguments - used when arguments are not in consistent order
    print(my_subtraction(arg2=15, arg1=10))

    say_hello("caleb", "nick", "jasper", "justin")


if __name__ == "__main__":
    main()
