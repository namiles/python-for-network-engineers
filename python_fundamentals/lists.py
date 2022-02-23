'''
Lists are a mutable sequence of objects and are surrounded by brackets [..]
'''

from os import sep


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


'''
Appending, Extending, and Inserting Lists

append() - Add a single element to the end of a list
extend() - Add elements of an interable, such as another list, to an existing list. You can extend with strings since they are iterable.
insert() - Inserts elements into a list at the specified index
'''
print("\nAppending, Extending, and Inserting")
list_of_devices = ["EdgeRouter", "CoreSwitch", "Distro1", "Distro2"]
print("Base List",list_of_devices)

# Append Access1 to the end
list_of_devices.append("Access1")
print("Appended:",list_of_devices)

access_switches = ["Access2","Access3"]
list_of_devices.extend(access_switches)
print("Extended:",list_of_devices)

# Insert Distro3 after existing two Distro elements
list_of_devices.insert(4, "Distro3")
print("Inserted:", list_of_devices)


'''
Popping, Removing, and Clearing Items

pop() - Remove the list item at the specified index, or remove the last item if not index is provided
remove() - Remove item in the list with the specified value. If there are duplicates, it removes the first ocurrence.
clear() - Clears all items from a list

'''
print("\nPopping, Removing, and Clearing Items in a List")
vlan_list = ["vlan10", "vlan20", "vlan30", "vlan40"]
print(vlan_list)
print("pop():", vlan_list.pop())
print("list after pop():", vlan_list)
print("pop(1):", vlan_list.pop(1))
print("list after pop(1):", vlan_list)

vlan_list2 = ["vlan50", "vlan60", "vlan70", "vlan80"]
print("\n",vlan_list2, sep="")
vlan_list2.remove("vlan60")
print("remove('vlan60'):", vlan_list2)

vlan_list2.clear()
print("cleared:", vlan_list2)


'''
Sorting Lists

The sort() method can be used to sort items in a list.
- If all items are numerical, it will sorts lowest to greatest by default
- Like min and max, capitals are considered to be lower in value than lowercase, so they will come first when sorted.

'''
print("\nSorting Lists")
list_of_acls = ["accessList50", "accessList20", "accessList100", "AccessList3"]
print(list_of_acls)
list_of_acls.sort()
print("sorted", list_of_acls)


'''
Nested Lists

Since each item in a list can be any object, lists can be nested inside of others lists.
'''
print("\nNested Lists / Sublists")
main_list = ["item0", "item1", ["sublist_item0","sublist_item1"], "item3"]
for item in main_list:
    print(item)
    if type(item) == list:
        print("List item found. Looping through it.")
        for item in item:
            print(item)

print(main_list[2][0])