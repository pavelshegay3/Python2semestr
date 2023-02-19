# 1
print("nomer1")
n = int(input("input N: "))
x1 = [pow(i, 2) for i in range(1, n + 1)]
print(x1, '\n\nnomer2')
# 2
n = int(input("input N: "))
x2 = [i for i in range(0, n + 1) if i % 2 == 0]
print(x2, '\n\nnomer3')


# 3
def moyafun(n):
    x3 = [i for i in range(0, n + 1) if i % 3 == 0 and i % 4 == 0]
    return x3


n = int(input("input n: "))
print(moyafun(n), '\n\nnomer4')
# 4
print("tbc\n\nnomer5")
# 5
n = int(input("input n: "))
x5 = [abs(i) for i in range(-n, 0 + 1)]
print(x5)
