# Python problem.
# Please print the power(a^b).

a = int(input("Enter base: "))
b = int(input("Enter power: "))

result = 1

for i in range(b):
    result = result * a

print("Answer:", result)

# seconnd Question.
# simple calculator.

# Simple Calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)

elif op == "-":
    print("Result:", a - b)

elif op == "*":
    print("Result:", a * b)

elif op == "/":
    print("Result:", a / b)

else:
    print("Invalid operator")
