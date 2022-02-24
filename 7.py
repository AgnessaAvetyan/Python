#!/usr/bin/python3

#3.Write a function that returns nth lowest number of a list. Return the lowest if second argument not specified. (use argparse module)

import argparse

def parsing():
    parser = argparse.ArgumentParser(prog = "Lower", description = "Find n-th lowest element")
    parser.add_argument("--index", metavar = "N-th element", required = True, type = int, help = "n-th lowest element")
    return parser.parse_args()

def n_th_min(my_list, arg):
    my_list.sort()
    if arg > len(my_list):
        return "Index out of list range"
    return my_list[arg - 1]

def main():
    arg = parsing().index
    my_list = [98,44,654,65,43,13,28,19,65132,0,321,65,1,651,65,41,32,0,321,35,4,654,13]
    print(n_th_min(my_list, arg))

if __name__ == "__main__":
    main()
