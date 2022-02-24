#Write a Python function to check whether a string is a pangram or not. 
#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : "The quick brown fox jumps over the lazy dog"

def in_alphabet(in_str):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    in_str = in_str.upper()
    i = 0
    while i < len(alpha):
        index = in_str.find(alpha[i])
        i += 1
        if index != -1:
            continue
        else:
            break
    return i == len(alpha) 

in_str = input("Enter the sentence:\n")
if in_alphabet(in_str):
    print("String is a pangram")
else:
    print("String is not a pangram")
