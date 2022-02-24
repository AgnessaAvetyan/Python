#Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).

def f_square(n_list: list) -> list:
    r_list = []
    i = 0
    for i in range(len(n_list)):
        r_list.append(f"{n_list[i]}'s square is: {n_list[i] * n_list[i]}") 
    return r_list

res = f_square([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
for i in range(len(res)):
    print(res[i])
