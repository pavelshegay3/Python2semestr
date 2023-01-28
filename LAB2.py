# Python Lists
# ex1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
# ex2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
# ex3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
# ex4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
# ex5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
# ex6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
# ex7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
# ex8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

# Python Tuples
# ex1
fruits = ("apple", "banana", "cherry")
print(fruits[0])
# ex2
fruits = ("apple", "banana", "cherry")
print(len(fruits))
# ex3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
# ex4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

# Python Sets
# ex1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")
# ex2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
# ex3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
# ex4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
# ex5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

# Python Dictionaries
# ex1
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.get("model"))
# ex2
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["year"] = 2020
# ex3
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["color"] = "red"
# ex4
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.pop("model")
# ex5
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.clear()

# Pythom While Loops
# ex1
i = 1
while i < 6:
    print(i)
    i += 1
# ex2
i = 1
while i < 6:
    if i == 3:
        break
    i += 1
# ex3
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# ex4
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# Python For Loops
# ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
# ex2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
# ex3
for x in range(6):
    print(x)
# ex4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
