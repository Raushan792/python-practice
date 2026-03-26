# Python problem.
# lenear search.
# Question 1.


 a = [22,43,54,56,46,88,77,66,99]
 search = 46
 for i in range(len(a)):
     if a[i] == search:
         print(f"Element found at index {i}")
         break
 else:
     print("Element not found and not exist")

# Question 2.
# Bubble sort.

 a = [2,33,454,744,3,45,63,15,25,22,65,332,874]   

 for j in range(len(a)-1):
     for i in range(len(a)-1-j):
         if a[i] < a[i+1]:
             a[i],a[i+1] = a[i+1],a[i]
 print(a)            
