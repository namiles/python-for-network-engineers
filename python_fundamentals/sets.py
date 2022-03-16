'''
Sets are an unordered collection of unique elements.

Sets temselves are mutable, but the elements inside a set must be immutable
Sets use { }, just like dicts.
Sets cannot contain duplicates.

To create an empty set, you must use my_set = set()
Using my_set = {} will create a dict.
'''

ip_addresses = {"192.168.1.1", "192.168.1.2", "192.168.1.240", "192.168.1.254"}

'''
Adding and Removing from Sets
'''
print("\nAdding and Removing from Sets")
print(ip_addresses)
ip_addresses.add("192.168.1.50")
print("Added 192.168.1.50:", ip_addresses)

# pop() removes a random element from a set and cannot specify what to pop.
print(ip_addresses)
print("Removed IP:",ip_addresses.pop())
print(ip_addresses)

'''
Other operations sets can use:
intersection() - Returns what is common between two sets
difference() - Returns what is not present in the passed in set
union() - Returns a union of the sets (with unique elements)
'''