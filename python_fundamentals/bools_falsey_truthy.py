
# Bool() can be used to determine if an object is falsey, or truthy.
# The bool class is a subclass of int

print("\nAll intergers except for 0 are considered truthy.")
# Falsey
print(bool(0))
# Truthy
print(bool(225))

print("\nAll floats except for 0.0 are considered truthy.")
# Falsey
print(bool(0.0))
# Truthy
print(bool(225.1))

print("\nEmpty sets and lists are considered falsey, unless they contain objects")
# Falsey
print("Empty list:",bool([]))
print("Empty tuple:",bool(()))
print("Empty dict:",bool({})) #empty dict
print("Empty set:",bool(set()))
# Truthy
print(bool(["apple"]))
print(bool(("banana")))

# == is used to make a comparisons
print("Does 2 == 2? -", bool(2 == 2))

# None keyword is always false
print("None is always:",bool(None))


print("\nAND, OR, and NOT Operators")
string1 = "hello" #truthy 
string2 = "" #falsey because it is empty

# AND returns true if all objects are true
print(bool(string1 and string2))
if string1 and string2:
    print("AND: Both strings are truthy")
else:
    print("AND: Both strings were not truthy")

# OR returns true if at least one operand is true
if string1 or string2:
    print("OR: At least one string is truthy")
else:
    print("OR: Both objects are not truthy")

# NOT is used to reserve the result of a boolean value
if not string1:
    print("NOT: This will print if string1 is false")
else:
    print("NOT: This will print if string1 is true")


