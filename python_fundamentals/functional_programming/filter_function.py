"""
Filter Function

The filter() function is used to filter a sequence with the help of a function that tests each element
to be true or false.

Similarly to the map() function, filter() returns an iterator containing elements that were true when 
ran through the function.
"""


def is_even(num):
    if num % 2 == 0:
        return True
    return False


def main():
    numbers = [12, 36, 8, 47, 6, 7, 1, 34, 83]
    # Syntax: filter(function, iterable)
    # This example is cast into a list and then printed.
    filtered_list = list(filter(is_even, numbers))
    print(filtered_list)

    # Example from comprehensions.py using filter() and lambda functions instead.
    interface_list = [
        "Loopback0",
        "Loopback1",
        "GigabitEthernet0/0",
        "GigabitEthernet0/1",
    ]
    gig_interfaces = list(filter(lambda x: x.startswith("Gig"), interface_list))
    print(gig_interfaces)


if __name__ == "__main__":
    main()
