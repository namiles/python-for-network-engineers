"""
Scope is referring to where objects are accessible from inside a module

4 Types of Scopes -- narrowest to broadest
local       Inside the current function
enclosing   Inside the enclosing functions
global      Top level of the module
built-in    Inside the builtins module
"""

# Global Variable
count = 0


def show_count():
    print(count)


def set_count(c):
    global count
    count = c


def main():
    # When functions cannot locate the object in the local scope, it goes up to the next --> enclosing --> global, etc
    # In this case, count exists in the global scope
    show_count()

    # Setting the count does NOT set the variable to 5 in the global scope, but will only set it in the function's local scope
    # You must add "global count" into the function if you want it to use the global scope
    set_count(20)

    # Print after setting a new value
    show_count()


if __name__ == "__main__":
    main()
