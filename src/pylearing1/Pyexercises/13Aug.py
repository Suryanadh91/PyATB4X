import math

name = input("what is your name")
print("My name is",name)
print('####################################')
# formating of string
num = 3.14159
format_num = f"{num:.2f}"
print(format_num)
print('####################################')
# Task 1
print("2 * 1", '=', 2 * 1)
print("2 * 2", '=', 2 * 2)
print("2 * 3", '=', 2 * 3)
print("2 * 4", '=', 2 * 4)
print("2 * 5", '=', 2 * 5)
print("2 * 6", '=', 2 * 6)
print("2 * 7", '=', 2 * 7)
print("2 * 8", '=', 2 * 8)
print("2 * 9", '=', 2 * 9)
print("2 * 10", '=', 2 * 10)
# table using str format
table = int(input())
print(f"{table}*1={table*1}")
print(f"{table}*2={table*2}")
print(f"{table}*3={table*3}")
print(f"{table}*4={table*4}")
print(f"{table}*5={table*5}")
print(f"{table}*6={table*6}")
print(f"{table}*7={table*7}")
print(f"{table}*8={table*8}")
print(f"{table}*9={table*9}")
print(f"{table}*10={table*10}")

# Task 2
a = int(input("num1"))
b = int(input("num2"))
summation  = a + b
sub = a - b
multiplication = a * b
div = a / b
print(summation)
print(sub)
print(multiplication)
print(div)
print(max(a,b))
print(pow(a,b))
print('####################################')

'''
Task 3
= is used to assign a value 
== is used to compare
** is used as power of 
'''
# Task 4 area of circle
pi = 3.14
r = float(input("Radius" ))
area = pi * (r**2)
print(area)
print('####################################')
pi = 3.14
r = float(input("Radius" ))
area = pi * pow(r,2)
print(area)
print('####################################')
r = float(input("Radius" ))
print(math.pi)
area = math.pi*pow(r,2)
print(area)
print('####################################')


