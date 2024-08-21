# Task 7 find the leap year

year = int(input("Enter the year\n"))
if year % 4 == 0 and year % 100!= 0:
    print("Leap year")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("leap year")
else:
    print("not leap year")

# Task 8 find the type of triangle
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

# Task 9
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
         print('Buzz')
    else:
        print(number)