# find the type of triangle

side_1 = int(input("enter side1 dimensions\n"))
side_2 = int(input("enter side2 dimensions\n"))
side_3 = int(input("enter side3 dimensions\n"))
if side_1 == side_2 == side_3:
    print("equal triangle")
elif (side_1 == side_2 and  side_1 != side_3
      or ((((side_1 == side_3 and side_1 != side_2
        or side_2 == side_1 and side_2 != side_3)
        or side_2 == side_3 and side_2 != side_1)
        or side_3 == side_1 and side_3 != side_2)
        or side_3 == side_2 and side_3 != side_1)):
    print("iso_traiangle")
elif side_1 != side_2 != side_3:
    print("scalen_triangle")
else:
    print("Invalid data")

# Factorial
n = 5
a = 1
for i in range (1,n+1):
    a = a * i
print(a)
