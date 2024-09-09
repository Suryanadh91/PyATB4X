n=int(input("Enter number:"))
fact=1
while(n>0):
    fact=fact*n
    n=n-1
    print(fact)
print("Factorial of the number is: ",fact)


num = int(input("Enter the num\n"))
factorial = 1
for i in range(1,num+1):
    print(i, end= ' ')
    factorial = factorial * i
print("\n",factorial)

import math
def fact(n):
    return (math.factorial(n))
num = int(input("Enter the number:"))
f = fact(num)
print("Factorial of", num, "is", f)

## Fibonacci series
a = [ ]
for i in range(8):
    if i <= 1:
        a.append(i)
    else:
        a.append(a[-1]+a[-2])
print(a)
