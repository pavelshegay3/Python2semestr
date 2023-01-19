# Python Syntax
# ex1
print("Hello World")
# ex2
if 5 > 2:
    print("Five is greater than two!")

# Python Comments
# ex1
# This is a comment
# ex2
"""
This is a comment
written in 
more that just one line
"""

# Python Variables
# ex1
carname = "Volvo"
# ex2
x = 50
# ex3
x = 5
y = 10
print(x + y)
# ex4
x = 5
y = 10
z = x + y
print(z)
# ex5
myfirst_name = "John"
# ex6
x = y = z = "Orange"
# ex7
def myfunc():
    global x
    x = "fantastic"


# Python Data Types
# ex1
x = 5
print(type(x))
# the data type would be int
# ex2
x = "Hello World"
print(type(x))
# the data type would be str
# ex3
x = 20.5
print(type(x))
# the data type would be float
# ex4
x = ["apple", "banana", "cherry"]
print(type(x))
# the data type would be list
# ex5
x = ("apple", "banana", "cherry")
print(type(x))
# the data type would be tuple
# ex6
x = {"name": "John", "age": 36}
print(type(x))
# the data type would be dict
# ex7
x = True
print(type(x))
# the data type would be bool

# Python Numbers
# ex1
x = 5
x = float(x)
# ex2
x = 5.5
x = int(x)
# ex3
x = 5
x = complex(x)

# Python Strings
# ex1
x = "Hello World"
print(len(x))
# ex2
txt = "Hello World"
x = (txt[0])
# ex3
txt = "Hello World"
x = txt[2:5]
# ex4
txt = "Hello World"
x = txt.strip()
# ex5
txt = "Hello World"
txt = txt.upper()
# ex6
txt = "Hello World"
txt = txt.lower()
# ex7
txt = "Hello World"
txt = txt.replace("H", "J")
# ex8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# Python Booleans
# ex1
print(10 > 9)
# The statement would print a Boolean value True
# ex2
print(10 == 9)
# The statement would print a Boolean value False
# ex3
print(10 < 9)
# The statement would print a Boolean value False
# ex4
print(bool("abc"))
# The statement would print a Boolean value True
# ex5
print(bool(0))
# The statement would print a Boolean value False

# Python Operators
# ex1
print(10 * 5)
# ex2
print(10 / 2)
# ex3
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")
# ex4
if 5 != 10:
    print("5 and 10 is not equal")
# ex5
if 5 == 10 or 4 == 4:
    print("At least one of the statements is true!")

# Python If...Else
# ex1
a = 50
b = 10
if a > b:
    print("Hello World")
# ex2
a = 50
b = 10
if a != b:
    print("Hello World")
# ex3
a = 50
b = 10
if a == b:
    print("Yes")
else:
    print("No")
# ex4
a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")
# ex5
a = b = c = d = 1
if a == b and c == d:
    print("Hello")
# ex6
if a == b or c == d:
    print("Hello")
# ex7
if 5 > 2:
    print("Five is greater than two!")
# ex8
if 5 > 2: print("Five is greater than two!")
# ex9
print("Yes") if 5 > 2 else print("No")
