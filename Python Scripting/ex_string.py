'''
Course: Complete Python Scripting for Automation
Name: Paul Barrionuevo
Program Description: String manipulation
Details: String manipulation, slicing, deleting and display
Software Development Environment: macOS Monterrey - Visual Studio
Solution File: ex_string.py
Date: 01/4/23
'''


'''
my_name= 'Paul Barrio'
my_new_name="Gondor developer"
my_info= """
Started my carrer as a lawyer but moved to tech
Inside of the tech industry, programming and drones were my call
"""

print(f'My name is: {my_name}\nMy new name is: {my_new_name}\nAnd my info is transcribed as: {my_info}')
'''

## SLICING OF A STRING
my_sliced_string="Hello world of Narnia"

print(my_sliced_string[0:-1])
print(my_sliced_string[0:7])
print(my_sliced_string[6])

## CHANGE OR DELETE STRINGS
### Can only delete the total string or assigned it to a new value

#del my_sliced_string
my_sliced_string = "Hello world"
print(my_sliced_string)

### String length
string_length = len("Hello world")
print(f'Length of this new string is {string_length}')

