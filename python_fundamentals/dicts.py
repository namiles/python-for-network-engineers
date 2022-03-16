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


'''
Iterating over Dictionaries
'''
print("\nIterating over Dicts")
device_info = {
    "device_type": "router",
    "model": "xr",
    "serial": "SDF12454",
}

# Iterating over Keys
print("-- for keys in device_info.keys():")
for key in device_info.keys():
    print(key)

# Iterating over Values
print("-- for keys in device_info.values():")
for value in device_info.values():
    print(value)

# Iterating over Keys and Values
print("-- for keys in device_info.items():")
for k,v in device_info.items():
    print(f"The {k} key has a value of {v}")


'''
Unpacking Dictionaries
'''
print("\nUnpacking Dicts")
switch1_info = {
    "device_type": "switch",
    "hostname": "S1",
    "model": "catalyst",
    "serial": "CCS12454",
}

switch2_info = {
    "device_type2": "switch",
    "hostname2": "S2",
    "model2": "catalyst",
    "serial2": "CCS15464",
}

# Because dicts must have unique keys, I added a "2" at the end of the switch2_info keys
# to demonstrate dict unpacking.
all_switches = {**switch1_info, **switch2_info}
print(all_switches)

