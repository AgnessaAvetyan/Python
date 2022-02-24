# Write a Python program to find the elements in a given set that are not in another set.

set1 = []
set2 = [] 

n = input("Enter set1's element ")
while n:
    set1.append(n)
    n = input("Enter set1's element ")
s1 = set(set1)

m = input("Enter set2's element ")
while m:
    set2.append(m)
    m = input("Enter set2's element ")
s2 = set(set2)

s1.difference(s2)
print(f"Set1 is: {s1}")
