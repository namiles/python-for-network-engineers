"""
Functions are constructs in programming that allows code to be broken up into functional pieces.
This helps maintain code reusability and modularity.

In Python, Functions can be a few things:
- Built-in --> Functions that are built into python
- 3rd Party --> Functions proivded by 3rd party libraries/modules
- Customer --> Functions a developer can define and use

** All functions in Python must return something, by default that is None **

Syntax
- Must not start with a number
- Must not be a reserved python word such as print, input, type, etc.
- Can be any combination of letters, numbers, underscores, or dashes.
- Create with the "def" keyword (Ex: def get_hostname(): )


PEP8 Styling for Functions
- Lowercase with words separated by underscores (Ex: retrieve_device_statistics())
- Use one leading underscore for non-public methods and instance variables (Ex: _get_devices())


Positional arguments must come before keyword arguments if using both.
"""

# Create the function
def my_function():
    """
    Prints "hello, this is my_function()" --> docstring
    """
    print("Hello, this is my_function()")


"""
The Return statement is used to return a value
All functions must return something
If not return is specified, None is return by defaut.
"""
def generate_email(username, provider="gmail"):
    email = f"{username}@{provider}.com"
    return email


def my_addition(arg1, arg2):
    sum = arg1 + arg2
    return sum  # pass an arugment back to code that calls function


def my_subtraction(arg1, arg2):
    result = arg1 - arg2
    return result


"""
Unknown Amount of Arguments
Functions can use the unpacking operator (*) to unpack variable length iterables and (**) to unpack variable length keyword arguments.
"""
def say_hello(*args):
    for arg in args:
        print("hello ", arg, "!", sep="")


"""
my_addition and my_subtration can be re-written to support an unknown amount of arugments using *args.
"""
def my_additon2(*args):
    total = 0
    for arg in args:
        total += arg
    return total


def my_subtraction2(*args):
    total = 0
    for arg in args:
        total -= arg
    return total


def print_details(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}: {v}")

"""
Default values can be used in Function Arguments
"""
def say_goodbye(name="default"):
    print(f"Goodbye {name}!")

"""
Returning Multiple Values
Functions can return more than one value
"""
def add_and_subtract(*args):
    added_total = 0
    subtracted_total = 0
    for arg in args:
        added_total += arg
        subtracted_total -= arg
    return added_total, subtracted_total

def main():
    # Simply call functions by referencing them
    my_function()

    print(my_addition(5, 5))

    # Keyword Arguments - used when arguments are not in consistent order
    print(my_subtraction(arg2=15, arg1=10))

    say_hello("caleb", "nick", "jasper", "justin")
    print(my_additon2(10, 20, 30, 40))
    print(my_subtraction2(10, 20, 30, 40))
    print_details(name="John Doe", job="Network Engineer", age="30")

    say_goodbye()  # No name is passed in, so the value of name will be "default" as specified in the function.

    # generated_email will contain the value returned from the generate_email() function
    generated_email = generate_email("pythonguy")
    print(generated_email)

    multiple_returns=add_and_subtract(2,3,4)
    # Python returns the multiple values inside a tuple
    print(type(multiple_returns))
    print(multiple_returns)


if __name__ == "__main__":
    main()
