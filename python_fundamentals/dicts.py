'''
Dictionaries are an unordered collection of key:value pairs that are surrounded by curly bracces {..}

Values are accessible by keys
Cannot have duplicate keys in a single dict
Keys must be immutable, such as strings, integers, and tuples
Values can be immutable
Order is not important, unless you're using an OrderedDict
'''
 
dict1 = {
    "key1":"value1",
    "key2":"value2",
}
print(dict1["key1"])

# The dict constructor can be used to convert other collections into to dictionaries:
names_and_ages = [('Alice', 32), ('Bob', 24), ('Charlies', 42)]
print(names_and_ages)
converted_dict = dict(names_and_ages)
print(converted_dict)


'''
Adding keys and accessing values
'''
print("\nAdding Keys and Accessing values")
device = {
    "hostname":"192.168.1.1",
    "username":"John",
    "password": "Doe"
}
print(device)
print(device["hostname"])
print(device["username"])
print(device["password"])

# To create a new key, use square brackets and specifiy the key value.
device["platform"] = "Cisco IOS"
print(device)

# The get() method can be used to retrieve the value of a specified key. Returns None if it does not exist.
print(device.get("hostname"))
print(device.get("version"))


'''
Removing Keys from a Dict
'''
print("\nRemoving Keys")
device2 = {
    "hostname":"192.168.1.2",
    "username":"John",
    "password": "Smith"
}
print(device2)

# pop() can be used to remove the specified key:value pair
# Just like in lists, it will return the value of what's being removed.
device2.pop("password")

print("pop('password'):", device2)


'''
keys, values, and items methods

These methods do not manipulate the dictionary in any way.
'''
print("\nkeys(), values(), and items() methods")
device3 = {
    "hostname":"192.168.1.3",
    "username":"John",
    "password": "Foo"
}
print(device3)

print("keys:", device3.keys())
print("values:", device3.values())
print("items:", device3.items())