# Write a Python function that takes a list and returns a new list with unique elements of the first list.

in_list = []
n = input("If You want to end, write 'exit'\ninput first member in list: ")

while n != "exit":
    if n.isnumeric():
        in_list.append(int(n))
    elif n != "exit":
        in_list.append(n)
    n = input("input list next member! ")
print(f"List is: {in_list}")


def unique_list(in_list):
    out_list = []
    for item in in_list:
        if item not in out_list:
            out_list.append(item)
    return out_list


print(f"Unique list is: {unique_list(in_list)}")
