import os
import string

# '''
'''
print("My Path: C:\TESTPATH")
# 1
print('1)')
x = 'C:\TESTPATH'
print("////only directories: ")
for i in os.listdir(x):
    if os.path.isdir(os.path.join(x, i)):
        print(i)
print("////only files: ")
for i in os.listdir(x):
    if os.path.isfile(os.path.join(x, i)):
        print(i)
print("////both: ")
for i in os.listdir(x):
    print(i)
print('\n2)')

# 2
x = input("enter a path: ")
if os.access(x, os.F_OK):
    print("////IT EXISTS")
else:
    print("////IT DOESN NOT EXIST")
if os.access(x, os.R_OK):
    print("////IT IS READABLE")
else:
    print("////IT IS NOT READABLE")
if os.access(x, os.W_OK):
    print("////IT IS WRITABLE")
else:
    print("////IT IS NOT WRITABLE")
if os.access(x, os.X_OK):
    print("////IT IS EXECUTABLE")
else:
    print("////IT IS NOT EXECUTABLE")
print('\n3)')

# 3
x = input("enter a path: ")
if os.access(x, os.F_OK):
    print('////IT EXISTS')
else:
    print('////IT DOES NOT EXIST')
filename = os.path.basename(x)
dirname = os.path.dirname(x)
print('////Filename of the path is:', filename)
print('////Directory name of the path is:', dirname, '\n\n4)')
# 4
print("Text file path: C:\TESTPATH")
path = 'C:\TESTPATH'
n = 0
f = input("input a text file name: ")
with open(os.path.join(path, f)) as x:
    for i in x:
        n = n + 1
print("////THERE ARE", n, "LINES IN THIS TEXT FILE")
print("\n5)")

# 5
f = input("input a text file name: ")
x = open(os.path.join(path, f), 'w')
string = input("input your list separated by space: ")
list = string.split()
for i in list:
    x.write(i)
    x.write('\n')
print("\n6)")

# 6
print('C:\TESTPATH\AZ')
path = input('input a directory where you want to create 26 text files from A to Z: ')
i = 0
letters = list(string.ascii_uppercase)
while i < 26:
    strl = letters[i]
    final = strl + ".txt"
    f = open(os.path.join(path, final), 'x')
    f.close()
    i = i + 1
print("\n7)")

# 7
path = 'C:\TESTPATH'
x1 = input('input a text file 1: ')
x2 = input('input a text file 2: ')
f1 = open(os.path.join(path, x1), 'r')
f2 = open(os.path.join(path, x2), 'w')
for i in f1:
    f2.write(i)
print("\n8)")
# 8
print("path is: C:\TESTPATH")
path = input("input a path where your file is located: ")
x = input("input a file name you want to delete: ")
if os.access(os.path.join(path, x), os.F_OK):
    print("////text file", x, "exists, deleting", x, "...")
    os.remove(os.path.join(path, x))
    print("////" + x, "has been deleted")
else:
    print("file",x,"or path",path,"were not found")
'''