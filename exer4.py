#Write a Python program to insert an element at a specified position into a given list. 

#Original list:
#[1, 1, 2, 3, 4, 4, 5, 1]
#After inserting an element at kth position in the said list:
#[1, 1, 12, 2, 3, 4, 4, 5, 1]

list1 = [1, 1, 2, 3, 4, 4, 5, 1]

item = input("Enter the item,which you want insert to list: ")
k = input("Enter index, where your item located: ")

if k.isnumeric() and item.isnumeric() and int(k) < len(list1):
    k = int(k)
    list1.insert(k,item)
    print(f"Changed list is:{list1}")
else:
    print("Invalid index or item")
