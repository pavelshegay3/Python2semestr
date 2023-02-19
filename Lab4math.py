# 1
import math

print("nomer1")
degr = int(input("input degree: "))
rad = float(degr * math.pi / 180)
print(degr, 'degree/degrees equal/equals', rad, 'radian\n\nnomer2')
# 2
h = int(input("input height: "))
bs1 = int(input("input base, first value: "))
bs2 = int(input("input base, second value: "))
area = float((bs1 + bs2) / 2 * h)
print("area of your trapezoid equals", area, '\n\nnomer3')
# 3
"""
area=p*a/2
p is perimeter = s*n
s is a length of 1 side
n is a number of sides
a is an apothem and equals s/(2*tan(180/n)) 
"""
n = int(input("input number of sides: "))
s = float(input("input the length of a side: "))


def areaofthepolygon(n, s):
    area = int((pow(s, 2) * n) / (4 * (math.tan(math.pi / n))))
    return area


print("the area of your polygon equals", areaofthepolygon(n, s), '\n\nnomer4')


# 4
def areaofaparallelogram(base, h):
    ar = float(base * h)
    return ar


base = int(input("input base: "))
height = int(input("input height: "))
print("area of your parallelogram equals", areaofaparallelogram(base, height))
