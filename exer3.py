#Write a Python program to remove the K'th element from a given list, print the new list. 
#Original list:
#[1, 1, 2, 3, 4, 4, 5, 1]
#After removing an element at the kth position of the said list:
#[1, 1, 3, 4, 4, 5, 1]

import copy

k = input("Which one element You want to remove ?: ")

list1 = [1, 1, 2, 3, 4, 4, 5, 1]
list2 = []
if k.isnumeric() and int(k) < len(list1):
    k = int(k)
    list1.remove(list1[k])
    list2 = copy.copy(list1)
    print(f"New list is: {list2}")
else:
    print("Invalid index")
