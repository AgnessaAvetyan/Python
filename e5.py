# Write a python program to find the power of a number using recursion.


def power_recursive(n, n_pow):
    if n_pow == 1:
        return n
    return n * power_recursive(n, n_pow - 1)


n = input("Please, Enter the number: ")
n_pow = input("Enter numbers's pow: ")

if n.isnumeric() and n_pow.isnumeric():
    n = int(n)
    n_pow = int(n_pow)
    print(f"{n}**{n_pow} = {power_recursive(n, n_pow)}")
else:
    print("Please enter only number!")
