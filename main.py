x = "Hello world"
y = len(x)
print(y)
# change test number one

x = "I love brawl stars"
# change test number two

# change test number three
"""lists
list items are ordered, changeable, and allow duplicate values
list items are indexed like in c
ordered means that the items have a defined order and that order will not change
if you add new items to a list the new items will be placed at the end of the list
"""
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
