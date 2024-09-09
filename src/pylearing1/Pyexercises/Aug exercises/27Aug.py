# find the highest number
num1 = int(input("Enter num 1"))
num2 = int(input("Enter num 2"))
num3 = int(input("Enter num 3"))

# 1 type of logic using max function
max_num = max(num1,num2,num3)
print(max_num)

# with if else
if num1 > num2 and num1 > num3:
    print("Max  is",num1)
elif num2 > num1 and num2 > num3:
    print("Max  is",num2)
else:
    print("Max  is",num3)

# program for grading the score
score = int(input("Give your score\n"))
if score >= 90 and score <= 100:
    print("A grade")
elif score >= 80 and score <= 89:
    print("B grade")
elif score >= 70 and score <= 79:
    print("C grade")
elif score >=60 and score <=69:
    print("D grade")
elif score >=0 and score <=59:
    print("F grade")
else:
    print("Invalid output")


# convert a+b+c to lambda

add = lambda a,b,c:a+b+c
print(add(1,2,3))
