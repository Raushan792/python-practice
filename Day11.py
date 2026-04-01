# Python Questions.
# ---------SETS-----------.
# Data structure.
# hash value.

a = hash("hello")
print(a)

b = hash((3,4,5,6,7,8,9))
print(b)

# Sets Traversing.
a = {1,2,4,6,7,8,"hello",9,3,4,5}
for i in a:
    print(i)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)          # {1, 2, 3, 4, 5, 6}
print("Intersection:", A & B)   # {3, 4}
print("Difference:", A - B)     # {1, 2}
print("Symmetric Difference:", A ^ B) # {1, 2, 5, 6}
