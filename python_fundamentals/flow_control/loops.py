
# range() function can be used in for loops to iterate a specified amount of times
for i in range(10,50): 
    print(i) #starts at 10, and ends at 50-1 (49)

print()

for i in range(10,50,5): 
    print(i) #starts at 10, and ends at 50-1 (49)

print()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print()

string = "This is my string"
for char in string:
  print(char)

print()

#Python does not support do..while or while..do loops. Must use While loops with breaks.
while True:
    response = input("Enter digits: ")
    if int(response) % 7 == 0:
        break
