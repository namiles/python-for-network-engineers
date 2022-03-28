"""
Map Function

The map() function is used to apply a function to an interable such as a list, tuple, etc.
It returns a map object, which is an iterator, with the results.

The map() function makes iterating easy and passes the iterating to the python interpretor.
"""


def squared(num):
    return num**2


def main():

    even_numbers = [2, 4, 6, 8, 10]

    # Syntax: map(function, iterable)
    map_object = map(squared, even_numbers)

    # The map object can be cast into a list
    new_list = list(map_object)

    print(even_numbers)
    print("Squared:", new_list)

    # map() and lambda functions can be used together
    odd_numbers = [1, 3, 5, 7, 9]
    odd_squared_list = list(map(lambda x: x**2, odd_numbers))
    print(odd_numbers)
    print(odd_squared_list)


if __name__ == "__main__":
    main()
