# Exercise 03 - Biography (Advanced Version)

# Ask the user for their details
name= input("Enter your name: ")
hometown = input("Enter your hometown: ")
age = int(input("Enter your age: ")) #use int() so its stored as a number

# Store the info in a dictionary
bio= {
    "name": name,
    "hometown" : hometown,
    "age": age
}

# Print all values
print("Name:", bio["name"])
print("Hometown:", bio["hometown"])
print("Age:", bio["age"])