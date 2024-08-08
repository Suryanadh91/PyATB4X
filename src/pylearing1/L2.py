import math

# # area of circle with radius 2
r = float(input("Radius" ))
print(math.pi)
area = math.pi*pow(r,2)
print(area)
# ####################################
pi = 3.14
r = float(input("Radius" ))
area = pi * pow(r,2)
print(area)
# ####################################
pi = 3.14
r = float(input("Radius" ))
area = pi * (r**2)
print(area)

# square and cube root of a number
number = float(input("number" ))
sq = number**2
sqroot = math.sqrt (number)
cube = math.pow(number,3)
print(sq)
print(sqroot)
print(cube)

## take 2 no.s print whether a is > or < or == to b
a = 5
b = 2
g = a > b
l = a < b
e = a == b
print("a greater than b", g)
print("a less than b", l)
print("a is equal to b", e)