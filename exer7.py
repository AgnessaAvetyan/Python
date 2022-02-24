#Write a Python program to remove the intersection of a 2nd set from the 1st set.

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

s1.symmetric_difference(s2)
print(f"Changed set is: {s1}") 
