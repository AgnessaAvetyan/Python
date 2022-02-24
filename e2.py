# Write a Python program to reverse a string.

in_str = input("Please, Enter any sentence You want\n")
out_str = ""
i = len(in_str) - 1

while i >= 0:
    out_str += in_str[i]
    i -= 1
print(f"Reverse string is:\n{out_str}")
