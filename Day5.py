# Questions python problem.
# Take a number as input and print its Table.

t = int(input("Enter a number here : "))
for i in range (1,11):
    print(t, "x", i ,"=",t*i)

# Sum of to n numbers.

n = int(input("Which you want : "))
sum = 0
for i in range (1,n+1):
    sum = sum + i
    print("your sum is ", sum)

# Factorial of numbers.

n = int(input("please tell your number : "))

fact = 1
for i in range (1,n+1):
    fact = fact * i
    print("your fact is ", fact)
