# Loops questions.
# python problems.
# Questions.
# check the number is prime or not.

n = int(input("check the number is prime or not : "))
count = 0
for i in range (1,n+1):
    if n % i == 0:
        count = count +1
if count == 2:
    print("the number is prime")
else:
    print("the number is not prime number")

# check string is palindrome.
a = "naman"
b = ""
for i in range (len(a)-1,-1,-1):
     b = b + a[i]
if a == b:
    print("it is palindrome")
else:
    print("its is not palindrome")

# While loopes questions.
# Accept a number and print its reverse.

a = int(input("Enter a number here :  "))
rev = 0
while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10
print(rev)

# separate each digit of a number and print it on the new line.
a = int(input("Enter a number here : "))
while a > 0:121
    print(a % 10)
    a = a // 10
