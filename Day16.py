# Python Questions.
# String Methods.

# endswith() - Return true if the string ends with the specified value.
a = "i like play cricket"
print(a.endswith("y",4,11))

# startswith - Return true if the string starts with the specified value.
b = "i believe in myself"
print(b.startswith("m",13,16))

# swap case() - Swap case , lower case becomes upper case and vise versa.
c = "How Old Are You My Friend"
print(c.swapcase())

# strip () - Returns a trimmed version of the string.
d = "******* Singh is King....... "
print(d.strip("*,., "))

# split () - Split the string at the specified separator and return a list.
k = "RCB#CSK#SRH#"
m = "hello.my name is milan singh.i am 11 year old"
p = "tree are so beautiful%india is great country"
print(k.split("#"))
print(m.split("."))
print(p.split("%"))

# l just - Returns a left justified version of the string.
s = "proud to be Rajputana"
x = s.ljust(8)
print(x,"culture")
