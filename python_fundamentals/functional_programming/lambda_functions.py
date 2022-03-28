"""
Lambda (aka Anonymous) Functions

In contrast to regular functions, Lambda functions are meant to be one-use and disposable.
Lambda functions are written on a single line in favor of being short and concise.
Lambda functions can be named or unnamed, hence also being known as Anonymous Functions
"""


def regular_function(name):
    """
    Example of a regular functions. Returns None by default.
    """
    print(f"Hello {name}! This is a regular function!")


def main():
    # regular_function("John")

    # lamba {parameters comma separated}: {What you want it to do}
    lamba_function = lambda name: print(f"Hello {name}! This is a lambda function!")
    lamba_function("Nick")

    # Lambda with a default parameter value
    squared = lambda x, y=2: x**y
    print(squared(2))
    print(squared(2, 3))


if __name__ == "__main__":
    main()
