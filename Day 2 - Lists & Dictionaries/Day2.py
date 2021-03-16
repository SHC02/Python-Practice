# Create my cart array
my_Cart = [12.99, 312, 251, 361.31]
# Sum of my cart components
print(sum(my_Cart))

# Adding component
my_Cart.append(39.99)
print(my_Cart)

# Printing how many components that array has
print(len(my_Cart))

# Printing 5th element of array
print(my_Cart[4])

# Play with element of array
print(my_Cart[0] * 10)

# How many bytes on your string?
my_String = "How many alphabets in this sentence"
print(len(my_String))

# Print specific location string from array
print(my_String[2])

# Create my Items list
my_Items = ["Mouse", "Laptop", "Microphone", "Screen", "Snack"]

# Create my products
my_Products = [my_Items, my_Cart]
print(my_Products)

# Dictionaries
my_List = [1,2,3,4,5]
my_Data = {"name": "Sehyun", "location": "Florida"}
print(my_Data["name"])

print(my_Data.keys())

print(list(my_Data.keys()))

# Adding another string element to the array
my_Data["occ"] = "student"
print(my_Data)

# Practice using different variables and make it together
user_1 = {"Name":"Tyler the Creator"}
user_2 = {"Name":"Frank Ocean"}
my_Users = [user_1 , user_2]
print(my_Users)