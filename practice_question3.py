"""
Write a program that prompts a user to enter their 
name and outputs “Found a” if the name contains “a”.
"""

# Answer: 
name = input("Enter your name: ")

if "a" in name:
    print("Found a")

# You can also add an else statement for when the name does not contain "a"

else:
    print("Did not find a")
