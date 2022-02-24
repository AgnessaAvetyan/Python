#/usr/bin/python3

#Write a program to create a new string made of the middle three characters of an input string.

import argparse

def parsing():
    parser = argparse.ArgumentParser(prog = "New string", description = "Mid characther of string")
    parser.add_argument("--string", metavar = "Change string", required = True, type = str, help = "Find middle 3 characters of string")
    return parser.parse_args()

def mid_3_char(my_string):
    l = len(my_string)
    if l < 3:
        return "Invalid string"
    if l % 2 == 0:
        return mid_3_char(my_string[l//2:])
    return my_string[l//2-1:l//2+2]

def main():
    print(mid_3_char(parsing().string))

if __name__ == "__main__":
    main()
