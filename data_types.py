# Numeric data type
a = 5
print("Type of a: ", type(a))

b = 5.0
print("Type of b: ", type(b))

c = 2 + 4j
print("Type of c: ", type(c))

# String data type
string1 = "My name is Abubakar"
string2 = "I'm learning Python"
string3 = '''Currently
            learning
            data
            type'''
print(string1, type(string1), end="\n")
print(string2, type(string2), end="\n")
print(string3, type(string3))

# Accessing elements of a string
print(string1[0])
print(string1[-1])

# List data type
List1 = ["data", "types", "in", "python"]
print(List1)
print(List1[0])
print(List1[2])
list2 = [['My', 'name'], ['is', 'Abubakar']]
print(list2)

# Print 'name' from list2
print(list2[0][1])
# Print first row
print(list2[0])
# Print first column
first_column = [sublist[0] for sublist in list2]
print(first_column)

# Accessing list using loop
for i in list2:
    print(i)

# Appending into a list
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a.append([7, 4, 1])
print(a)

# Extending a row
a[1].extend([9, 5, 1])
print(a)

# Reversing the order
a[1].reverse()
print(a)

# Exploring Tuple
tuple1 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(tuple1)
print(tuple1[1])
first_column = [subtuple[1] for subtuple in tuple1]
print(tuple1[0][1])

# Exploring sets
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set1)
set1.add(71)
print(set1)
set1.update([41, 51])
print(set1)
set1.remove(71)
print(set1)

set1 = {1, 2, 3}
set2 = {4, 5, 6}
unionset = set1.union(set2)
print(unionset)
intersectionset = set1.intersection(set2)
print(intersectionset)
subsetcheck = {2, 3}.issubset(set1)
print(subsetcheck)

# Exploring Dictionary
dict1 = {"Abubakar": 27, "Ali": 26, "Waqas": 30}
print(dict1)
print(dict1["Waqas"])
# Adding into dictionary
dict1["Umer"] = 32
print(dict1)

for value in dict1.values():
    print(value)
