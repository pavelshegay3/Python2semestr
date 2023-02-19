"""
# 1.A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    print(ounces)


grams = float(input("input grams: "))
grams_to_ounces(grams)


# 2.Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)
def f_to_c(fr):
    celc = (5 / 9) * (fr - 32)
    print(int(celc))


fahrenheit = float(input("input F: "))
f_to_c(fahrenheit)


# 3.Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
def countrabandch(heads, legs):
    # every chicken has 2 legs and 1 head, every rabbit - 4 legs and 1 head
    legs_chicken_and_halfofrabbits = heads * 2
    halfofrabbitslegs = legs - legs_chicken_and_halfofrabbits
    numofrab = halfofrabbitslegs / 2
    numofch = heads - numofrab
    print("We have ", int(numofch), "of chickens and", int(numofrab), "of rabbits in the area")


H = int(input("enter heads:"))
L = int(input("enter legs:"))
countrabandch(H, L)
# 4.You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
def checkprime(a):
    if a <= 1:
        return False
    b = 0
    for i in range(2, a):
        if a % i == 0:
            return False
            break
    return True


def myfunction1(lis):
    for x in lis:
        if checkprime(x):
            print(x)


stringofnums = input("enter your list: ")
mynumbers = stringofnums.split()
for i in range(len(mynumbers)):
    mynumbers[i] = int(mynumbers[i])
myfunction1(mynumbers)
"""

"""
# 7.Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def checkfor33(list):
    for i in range(len(list) - 1):
        if list[i] == 3:
            if list[i + 1] == 3:
                return True
    return False


stringofnums = input("enter your list: ")
mylist = stringofnums.split()
for i in range(len(mylist)):
    mylist[i] = int(mylist[i])
print(checkfor33(mylist))
"""

"""
# 8. Write a function that takes in a list of integers and returns True if it contains 007 in order
def has007(list):
    for i in range(len(list) - 2):
        if list[i] == 0:
            if list[i + 1] == 0:
                if list[i + 2] == 7:
                    return True
    return False


stringofnums = input("enter your list: ")
mylist = stringofnums.split()2 
for i in range(len(mylist)):
    mylist[i] = int(mylist[i])
print(has007(mylist))
"""

"""
# 9. Write a function that computes the volume of a sphere given its radius.
def volume(rad, pi):
    V = (4 / 3) * pi * pow(rad, 3)
    print(int(V))


rad = float(input("Vvedite radius:"))
pi = 3.14
volume(rad, pi)
"""

"""
# 10.Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.
def uni(mylist):
    return list(dict.fromkeys(mylist))


stringofnums = input("enter your list: ")
mylist = stringofnums.split()
for i in range(len(mylist)):
    mylist[i] = int(mylist[i])
print(uni(mylist))
"""

"""
# 11. Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
def isp(s):
    return s == s[::-1]


s = str(input("enter your string: "))
print(isp(s))
"""

"""
# 12. Define a functino histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
def star(n):
    m = ""
    for i in range(0, n):
        m = m + "*"
    print(m)


def his(list):
    for i in list:
        star(i)


stringofnums = input("enter your list: ")
mylist = stringofnums.split()
for i in range(len(mylist)):
    mylist[i] = int(mylist[i])
his(mylist)
"""
# 13. Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
from random import randint


def lob(g, d):
    if g < d:
        print("Your guess is too low.\nTake a guess.")
    if g > d:
        print("Your guess is too high.\nTake a guess.")


def game(name):
    a = 1
    guess = randint(1, 20)
    n = int(input())
    while n != guess:
        lob(n, guess)
        n1 = int(input())
        n = n1
        a = a + 1
    if n == guess:
        print("Good job, ", name, "! You guessed my number in ", a, " guesses!")


print("Hello! What is your name?")
name = str(input())
print("\n")
print("Well,", name, ", I am thinking of a number between 1 and 20.\nTake a guess.")
int
game(name)
