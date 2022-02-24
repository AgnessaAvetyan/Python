#/usr/bin/python3

#Write a program to unpack the following tuple into four variables and display each variable.
#Tuple1 = (10, 20, 30, 40)

def unpack_tuple(my_tuple):
    e = "a,b,c,d = my_tuple[0], my_tuple[1], my_tuple[2], my_tuple[3]\nprint(a,b,c,d)"
    exec(e)

def main():
    Tuple1 = (10, 20, 30, 40)
    unpack_tuple(Tuple1)

if __name__ == "__main__":
    main()
