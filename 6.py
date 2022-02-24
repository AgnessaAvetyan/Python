#!/usr/bin/python3

#2.Print all numbers from 1 to 1000 which reads the same in reversed form in both binary and decimal format.

def check():
    for i in range(1, 1001):
        if i == int(str(i)[::-1]) and bin(i)[2:] == bin(i)[2:][::-1]:
            print(i)
check()
