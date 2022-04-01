"""
File input and output

Opening, closing, reading from, and writing to files are all very useful skills to have in Python for network automation.
For example, you can write network device command output to a file, or read in a list of IP addresses.

Modes
- r = open for reading (default)
- w = open for writing (overwrites existing data)
- x = open for exclusive creation, failing if the file already exsits
- a = Open for writing, appending to the file if it exists

- b = Open in binary mode
- t = Open in text mode (default)
- + = Open for updating (read and write)

Although r is default, it is best practice to be explicit over implicit and specify the mode anyway.

"""


def main():
    # Opening and Closing files without a Context Manager

    # Take file to open as a string and specify mode. readdata is an object created to store the contents of the file
    file_data = open("textfile.txt", mode="r", encoding="utf-8")

    # The read() function can be used to print contents
    print("\nRead all contents:")
    print(file_data.read())

    # When using the open() function, you must use close() to cose the file when finished with it.
    file_data.close()

    # readline() reads only 1 line of a file at a time
    # You can use for loops to iterate through each line of a file
    print("\nRead line by line:")
    file_data_by_line = open("textfile.txt", "r")
    for line in file_data_by_line:
        print(line, end="")

    # You can also use readlines(), which returns each line of a file in list format.
    # If desired, you can also use a for loop here to loop through each item in the list.
    print("\n\nRead using readlines to return a list:")
    file_data_list = open("textfile.txt", "r")
    print(file_data_list.readlines())

    # print() for spacing
    print()

    """
    Keeping track of opening and closing files can be annoying.
    Python provides the with statement, also called a context manager. (with-blocks)
    It uses the open() function but doesn't require assigning to an object and automatically closes the file.
    """

    with open("context_manager_example.txt", "r") as f:
        print("\nData before writing:\n", f.read(), sep="")

    # a+ can be used to write to the file by appending.
    with open("context_manager_example.txt", "a+") as f:
        # Notice there is a newline at the beginner of the line. Appending does NOT put newlines in automatically.
        print(f.write("\nThis line was added using python."))

    # Read file after adding the line.
    with open("context_manager_example.txt", "r") as f:
        print("\nData after writing to do:\n", f.read(), sep="")

    """
    A Note on filepaths

    The above examples are using files that are in the working directroy, or the same directory that this python file lives in.
    If you need to work with a file that's not in same directroy as this file, you will need to use a filepath to acess it.

    - Releative File Path: Location of a file relative to where this script is.
    - Absolute File Path: Location of the file starting with the root directory
    """

    # This example shows reading the nested_file using the releative filepath.
    print("Reading Nested Files:")
    with open("nested_file_folder/nested_file.txt", "r") as f:
        print(f.read())

    # Using aboslute paths depends on the operating system you are using. Refer to the Python documention for more info.


if __name__ == "__main__":
    main()
