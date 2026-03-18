# Day 3 python problem.
# Question even and odd numbers.

numbers = int(input("Enter the  number here :-"))
if numbers % 2 == 0:
  print("This is even number")
else:
  print("This is odd numbers")
              
# Problem :- largest of three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)
