'''
Course: Complete Python Scripting for Automation
Name: Paul Barrionuevo
Program Description: Practice exercise 1
Details: Input user value and manipulate data
Software Development Environment: macOS Monterrey - Visual Studio
Solution File: string_practice.py.py
Date: 01/6/23
'''

import os

t_width = os.get_terminal_size().columns

print(t_width)

y = input("Enter a value: " )
print(y.center(t_width).title()) ## Starting letter becomes capital
print(y.rjust(t_width))
print(y.ljust(t_width))

## Command to find cols = tput cols