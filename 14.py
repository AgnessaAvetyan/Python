#!usr/bin/python

#1.Գրել ֆունկցիա, որը argparse-ի միջոցով կստանա  երկու արգումենտ՝ անուն և  տարիք, կվերադարձնի "mature", եթե տարիքը մեծ է 18-ից և կլցնի dictionary-ի մեջ անունը և տարիքը։ Ֆունկցիային տալ այլ անուն և դրանով կանչել main() ֆունկցիայում։

import argparse

def parsing():
    my_pars = argparse.ArgumentParser(prog = "Name&Age", description = "Bigger than 18")
    my_pars.add_argument("--name", metavar = "NAME", required = True, type = str, help = "Person's name")
    my_pars.add_argument("--age", metavar = "AGE", required = True, type = int, help = "Person's age")
    my_args = my_pars.parse_args()
    return my_args

def main():
    arguments = parsing()
    dict_1 = {}
    dict_1['name'] = arguments.name
    dict_1['age'] = arguments.age
    print(dict_1)
    if arguments.age > 18:
        print("mature")

if __name__ == "__main__":
    main()
