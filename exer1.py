#Write a Python program to create a list by concatenating a given list which range goes from 1 to n. 
#Sample list : ['p', 'q']
#n = 5 Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

n = input("Enter the count: ")

if n.isnumeric():
    n = int(n)
    i = 1
    list1 = []
    while i <= n:
    	list1.append(f"p{i}")
    	list1.append(f"q{i}")
    	i += 1
    print(f"List is:{list1}")	
else:
    print("Please enter only positive integer!")
