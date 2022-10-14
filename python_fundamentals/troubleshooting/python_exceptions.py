"""
Exceptions are a great way to catch when errors occur and handle them gracefully.
Python has many built-in exception types, and they can be hadnled indepenecy within try..except blocks.
Many python libraries, such as Netmiko, have custom exceptions as well.

try..except blocks are great to use for code that you except could produce an error.

try:
    {code that could produce an exception}
except {exeption, ex NameError}:
    {react to exception}
except {someo ther exception}:
    {react}
else:
    {code to run ONLY if there is no error}
finally:
    {code to run no matter if the try succueeds or fails}

You can catch general exceptions using "Exception", but that's not recommended:

try:
    {code}
except Exception:
    {react}

"""


def main():
    # In this example, we try to print "x", but x does not exist. This results in a "NameError" exception.
    try:
        print(x)
    except NameError:
        print("Tried printing an object that is not defined.")

    try:
        name = "Python"
        number = 2
        # Will produce an error becasue you can't add to different type of objects (TypeError)
        name + number
    except TypeError as e:
        print(f"Caught TypeError exception: {e}")


if __name__ == "__main__":
    main()
