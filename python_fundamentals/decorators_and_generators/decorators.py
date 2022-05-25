from rich import print as rprint
from time import perf_counter

"""
Decorators

Decorators are functions that take another function as an argument, and returns another function
"""
#Below is a basic example of a decorator
def my_first_function(func):
    def my_second_function():
        rprint("Beginning to execute function")
        func()
        rprint("The function has finished executing")
    return my_second_function()

def greeter():
    rprint("Hello world!")


"""
There is an easier way to use decorators by using the @ symbol and referencing the decorator you created.
"""
def prettify(func):
    def wrapper(*args, **kwargs):
        rprint("[cyan]***************************************[/cyan]")
        func(*args, **kwargs)
        rprint("[cyan]***************************************[/cyan]")
    return wrapper

@prettify
def banner():
    print("DO NOT ACCESS THIS DEVICE UNLESS AUTHORIZED")


"""
Accepting Arguments into a Decorated Function -- custon_banner() in this case

You can pass arguments into a decorated function, however the decorator must also except the arguments. 
You could just hard code an argument into the decorator, but that removes the flexibility of the function.
The solution is to use *args or **kwargs (on line 24) in the decorator function to support a variable amount of arguments.
"""
@prettify
def custom_banner(text):
    print(f"{text}")


"""
Performance Decorators are a good way to calculate how long a function takes to execute
"""
def performance_test(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        finish = perf_counter()
        performance = finish - start
        print(f"Execution time (s): {performance}")
    return wrapper

@performance_test
def print_some_numbers(num):
    for i in range(0, num):
        print(i)


"""
Generators are a lazy way to create new objects, but can be more resource efficient
Generators are a better option over a list because they do not require the memory footprint a list requires
Only requires memory for only one value they are yielding
"""

# List Example
def square_me(list_of_nums:list):
    my_list = []
    for num in list_of_nums:
        my_list.append(num * num)
    return my_list

# Geneerator functions is the yield keyword
# Return a generator object
# No calculations are actually done until the return generator object is looped through, wheere they are calculated on the fly
def square_generator(list_of_nums:list):
    for num in list_of_nums:
        yield (num * num)


if __name__ == "__main__":
    #my_first_function(greeter)

    rprint("[yellow]Decorators[/yellow]")
    # No need to reference the decorator function. Can call banner() directly
    banner()
    custom_banner("This is a private system for authorized users only.")

    # Performance Checker
    # print_some_numbers(2000)

    rprint("[yellow]Generators[/yellow]")
    # Generators
    print(square_me([1,2,3,4,5,6,7,8,9,10]))
    print(square_generator([1,2,3,4,5,6,7,8,9,10]))
    gen_object = square_generator([1,2,3,4,5,6,7,8,9,10])
    
    # You can loop through generator objects, where each value is calculated one at a time
    for value in gen_object:
        print(value)