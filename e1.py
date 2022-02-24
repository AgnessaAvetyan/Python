# Write a Python function to sum all the numbers in a list.

in_list = []
n = input("If You want to end, write 'exit'\ninput first member in list: ")

while n != "exit":
    if n.isnumeric():
        in_list.append(int(n))
    elif n != "exit":
        print("Please enter only number!")
    n = input("input list next member! ")
print(f"List is: {in_list}")


def f_sum(in_list=[]):
    r_sum = 0
    for i in range(len(in_list)):
        r_sum += in_list[i]
    return r_sum


print(f"List members sum is: {f_sum(in_list)}")
