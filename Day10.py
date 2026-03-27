# Tuple in python.
# -------------------------Tuple-------------------------
a = (1,2,3,4,print(),6.43,"hello")
for i in range (len(a)):
    print(a[i])

# index finding.

a = (2,3,45,56,6,677,76,656,76,76,76,76)
index = a.index(56)
print(index)

# count tuple.

b = (2,3,45,56,6,677,76,656,76,76,76,76)
count = b.count(76)
print(count)

# Tuple unpacking.

a,b,c,d = (2,3,4,5,)
print(c)
