'''
Lists are a mutable sequence of objects and are surrounded by brackets [..]
'''

random_list = [2, "hello", 2.34, "vlan 10", ["vlan 11,", "vlan12"], {"interface":"GigabitEthernet1/0"}]

# Iterating through a List
for item in random_list:
    print(f"{item} has a type of {type(item)}")

'''
Negative Indexing can be used to access elements of a list in reverse order
'''
print("\nNegative Indexing")
# Print last item of the list
print("Last item of the list:",random_list[-1]) 
print("Second to last item of the list:",random_list[-2])

'''
Slicing can be used with lists to access subsets of elements inside a list

[Starting #(inclusive) : Ending #(exclusive) : Step Value
'''
print("\nSlicing")
# Print the first four elements of the list
print(random_list[:4]) 

'''
Min and Max Functions

Min and Max functions are used to find the minimum and maximum values in a list.
With list containing only numeric values, it will return highest and lowest numeric values.
If a list is all strings, it will return values based on the first characters
A-Z > a-z -- Capital letters are considered to be lower than lowercase letters.
'''
numeric_list = [10, 5, 8, 74 ,65 , 14 , 64, 3]
print("\nMin and Max Functions")
print(numeric_list)
print("Minimum Value:", min(numeric_list))
print("Maximum Value:", max(numeric_list))

