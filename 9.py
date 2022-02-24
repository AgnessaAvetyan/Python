#/usr/bin/python3

#Concatenate two lists in the following order
#list1 = ["Hello ", "take "]
#list2 = ["Dear", "Sir"]
#['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

def list_concatenate(list_1, list_2):
    list_3 = []
    for i in list_1:
        for j in list_2:
            list_3.append(f"{i} {j}")
    return list_3

def main():
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]    
    print(f"Your lists is: {list1} {list2}\nYour concatenated list is: {list_concatenate(list1, list2)}")

if __name__ == "__main__":
    main()
