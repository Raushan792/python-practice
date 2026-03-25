# Python problems.
#  print positive and negative of a list.
t = [-23,44,-32,47,-86]
print(f"positive elements are : ")
for i in t:
    if i >= 0:
        print(i)
print(f"negative elements are : ")
for i in t:
    if i < 0:
        print(i)
        
# Question 2.        
# Find the greatest element and print its index too.

l = [23, 43, 433, 463, 742, 322, 875, 865, 887]

largest = l[0]
index = 0

for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]
        index = i

print(f"Your largest number is {largest} at index {index}")
