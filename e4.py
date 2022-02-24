# Create a recursive function.


def f_recursive(n):
    if n == 1:
        return 1
    return n * f_recursive(n - 1)


n = input("Please, Enter the number: ")
if n.isnumeric():
    n = int(n)
    print(f"n! = {f_recursive(n)}")
else:
    print("Please enter only number!")
