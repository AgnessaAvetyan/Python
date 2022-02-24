#Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. 

#Sample Items : green-red-yellow-black-white

#Expected Result : black-green-red-white-yellow

def f_input():
    str1 = input("Enter sentence like example: green-red-yellow-black-white\n")
    if str1.find(" ") != -1:
        return f_input()
    return "-".join(sorted(str1.split('-')))
        
print(f_input())
