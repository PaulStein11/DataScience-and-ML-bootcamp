'''
Course: Complete Python Scripting for Automation
Name: Paul Barrionuevo
Program Description: join, center and zfill(zero fill)
Details: join, center and zfill(zero fill)
Software Development Environment: macOS Monterrey - Visual Studio
Solution File: ex_join.py
Date: 01/6/23
'''


my_str="python"
y="-".join(my_str)
z="*".join(my_str)
x="\t".join(my_str)
w="\n".join(my_str)
print(w)
print(x)
print(y)
print(z)


my_new_str="python scripting"
p=my_new_str.center(50)
print(p)


'''
p
y
t
h
o
n
p       y       t       h       o       n
p-y-t-h-o-n
p*y*t*h*o*n
                 python scripting             
'''