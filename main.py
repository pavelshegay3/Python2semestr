"""
x = "Hello world"
y = len(x)
print(y)
# change test number one

x = "I love brawl stars"
# change test number two

# change test number three
""""""
list items are ordered, changeable, and allow duplicate values
list items are indexed like in c
ordered means that the items have a defined order and that order will not change
if you add new items to a list the new items will be placed at the end of the list
# create a list
thislist = ["apple", "banana", "cherry", "apple"]
print(thislist)
# list length
thislist = ["apple", "apple", "cherry", "banana"]
print(len(thislist))
# list items-data types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9]
list3 = [True, False, False]
# a list can contain different data types
list1 = ["abc", 34, True, 40, "male"]
# type of a list
mylist = ["water", "food"]
print(type(mylist))
# access items
print(thislist[1])
print(thislist[-1])
print(thislist[1:4])
print(thislist[:4])
print(thislist[1:])
print(thislist[-3:-1])
# check if a specified item is present in a list
if "apple" in thislist:
    print("apple is in the list")
# change item value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi"]
stringofnums = input("enter your list: ")
mynumbers = stringofnums.split()
for i in range(len(mynumbers)):
    mynumbers[i] = int(mynumbers[i])
print(mynumbers)

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)


class Mynumbers:
    def _iter_(self):
        self.a=1
        return self
    def _next_(self):
        x=self.a
        self.a+=1
        return x
meclass=MyNumbers()
myiter=iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# python regex
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$",txt)

string=['afas_afa','asfasf_fafasf']
for i in string:
    x=i.split("_")
    print(x)
"""