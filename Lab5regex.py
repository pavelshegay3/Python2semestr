import re

# 1
print("nomer1")


def nomer1(string):
    x = "ab*"
    if re.search(x, string):
        print("True")
    else:
        print("False")


nomer1("sa")
nomer1("sab")
nomer1("sabbb")
nomer1("aaaa")
nomer1("sadfasfbn")
nomer1("b")
nomer1("a")
nomer1("ad")
print("\n")
# 2
print("nomer2")


def nomer2(string):
    x = "ab{2}|ab{3}"
    if re.search(x, string):
        print("True")
    else:
        print("False")


nomer2("hello dab")
nomer2("hello dabb")
nomer2("hello daabbb")
nomer2("hello abbbbbbbb")
nomer2("hello")
nomer2("hello abbbsa")
# 3
print("\nnomer3")


def nomer3(string):
    x = "[a-z]+_[a-z]+"
    for i in string:
        if re.search(x, i):
            print(i, "is True")
        else:
            print(i, "is False")


string = ['aad_adfa', 'ddaF_dadf', 'asdfgfADfnh']
nomer3(string)
# 4
print("\nnomer4")


def nomer4(string):
    x = "[A-Z]{1}[a-z]+"
    for i in string:
        if re.search(x, i):
            print(i, "is True")
        else:
            print(i, "is False")


string = ['affaDFasdg', 'adgFFfda', 'dafvdGasd', 'aaD']
nomer4(string)
# 5
print('\nnomer5')


def nomer5(string):
    x = "a.*b$"
    for i in string:
        if re.search(x, i):
            print(i, "is True")
        else:
            print(i, "is False")


string = ['hfafafhb', 'adbcab', 'adhj', 'ab', 'b', 'a']
nomer5(string)
# 6
print('\nnomer6')


def nomer6(string):
    x = "[., ]"
    for i in string:
        print(i, "to", re.sub(x, ":", i))


string = ['dasdg as, ad. ', 'adabcva', 'n ad,']
nomer6(string)
# 7
print('\nnomer7')


def nomer7(string):
    words = string.split("_")
    print(words[0] + ''.join(i.capitalize() for i in words[1::]))


string = "hello_world"
nomer7(string)
# 8
print('\nnomer8')


def nomer8(string):
    for i in string:
        x = "[A-Z]"
        print(i, "to", re.split(x, i))


string = ['aBaBNaaaa', 'asdasfaf', 'aDFadFFg', 'FGDHKS']
nomer8(string)
# 9
print('\nnomer9')


def nomer9(string):
    x = "(\w)([A-Z])"
    for i in string:
        print(i, "to", re.sub(x, r"\1 \2", i))


string = ['winterIscoming', 'winteriscoming', 'winterIsComing']
nomer9(string)

# 10
print('\nnomer10')
# def nomer10(string):
