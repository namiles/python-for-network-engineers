"""
Python has a built-in debugger called the python debugger, or pbd.

Can be used to step through a script line by line to find exactly where something is going wrong.

pdb can be used in several ways:
- Imported (import pdb)
- Invoked as a script (python3 -m pdb mycode.py). Useful for modules that do not have breakpoints.

Useful Commands
- help
- (d)own --> move down one level
- (u)p --> move up one level
- (s)tep --> execute the current line, stop at the first possible occasion (like a fdunction that is called)
- (n)ext --> Continue exectuin until the next liune in the current function is reached or it returns
- (l)ist . --> List source code for the current file. Lists 11 lines around the current line without arguments.
- ll --> List all source code for the current function or frame
- p {expression} ---> Evaluate the expression in the current context and prtint its value
- pp {expression} --> Same as p, but prints it pretty. Useful for JSON data.

Note: The difference between step and next is that step stops INSIDE a called fujnction, while next executes called functions.

Docs:
https://docs.python.org/3/library/pdb.html
"""

# In Python3.7, "breakpoint()"is a built-in function to create a breakpoint vs. uning "import pdb; pdb.set_trace()"'
# Importing pdb is not needed to use breakpoint() in 3.7+


# import pdb


def example_function(device, command):
    print(f"Sending {command} to {device}")


def main():

    # Where breakpoints are set is important.

    # # Older Way
    # pdb.set_trace()

    # Newer Way
    breakpoint()

    print("\nThe Python Debugger")
    print("-" * 20, "\n")
    example_function("R1", "show run")


if __name__ == "__main__":
    main()
