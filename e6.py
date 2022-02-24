# Write a function, which will find the average of an unknown number of inputs .

in_list = []
count = 0
n = input("If You want to end, write 'exit'\ninput first member in list: ")

while n != "exit":
    if n.isnumeric():
        in_list.append(int(n))
        count += 1
    elif n != "exit":
        print("Enter only number!")
    n = input("input list next member! ")
print(f"List is: {in_list}")


def f_average(count, in_list=[]):
    r_sum = 0
    for i in range(len(in_list)):
        r_sum += in_list[i]
    return round(r_sum / count, 2)


print(f"List members average is: {f_average(count, in_list)}")
