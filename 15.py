#!/usr/bin/python3

#2.Գրել ծրագիր, որը որպես արգումենտ կստանա n քանակի կենդանիների անուններ, կդասակարգի ընտանի/վայրի, կվերա դ արձնի dict, որի key-երն են household և wild: Օգտ ա գործել add_argument-ի choices պ ա րա մետ րը։

import argparse

def parsing():
    parser = argparse.ArgumentParser(prog = "Animals", description = "Animals sorting")
    parser.add_argument("--animals", metavar = "Animals names", type = str, choices = ["Dog", "Horse", "Chicken", "Panda", "Monkey", "Rabbit", "Cat", "Bear", "Tiger", "Cow"], nargs = '+', help = "Sorting animals household and wild")
    return parser.parse_args()

def main():
    household, wild = [], []
    pars_args = parsing()
    animal_dict = {"household":["Dog", "Cat", "Rabbit", "Chicken", "Cow", "Horse"], "wild":["Bear", "Panda", "Monkey", "Tiger"]}
    for i in pars_args.animals:
        if i in animal_dict["wild"]:
            wild.append(i)
        elif i in animal_dict["household"]:
            household.append(i)
    print(f"This animals is wild: {wild} \nThis animals is household: {household}")
main()
