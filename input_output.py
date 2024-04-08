# Print function using double quotes
print("Hello, World!")

# Printing variables
name = "Abu Bakar"
age = 27
print("Name:", name, "Age:", age)

# print function using .format
print("Name: {} Age: {}".format(name, age))

# print function using f-string
print(f"Name: {name} Age: {age}")

# print using sep and end argument
print("Name:", name, "Age:", age, end="")
print("This is a new line")
print("Name:", name, "Age:", age, sep="-")

# Taking input from user using input()
num = int(input("Enter a number: "))
num = num + 5
print(num)

# Taking multiple inputs
x, y, z = input("Enter three numbers : ").split()
print(f"Print first number is: {x}")
print("Second number is: {}".format(y))
print("Third number is: ", z)
