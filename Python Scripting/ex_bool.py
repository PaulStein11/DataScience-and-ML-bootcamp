'''
Course: Complete Python Scripting for Automation
Name: Paul Barrionuevo
Program Description:  Boolean Operations
Details: Testing boolean methods on string values
Software Development Environment: macOS Monterrey - Visual Studio
Solution File: ex_bool.py
Date: 01/4/23
'''
my_string = "hello"

print(my_string.startswith("h"))
## True
print(my_string.startswith("hi"))
## False
print(my_string.endswith("o"))
## True
print(my_string.islower())
## True
print(my_string.isupper())
## False
print(my_string.istitle())
## False
print(my_string.isspace())
## False
print(my_string.isnumeric())
## False


'''
True
False
True
True
False
False
False
False
'''
