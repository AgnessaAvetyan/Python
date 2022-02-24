#!/usr/bin/python3

#4. Գրել ծրագիր, որը որպես արգումենտ կստանա գրքի վերնագիր, հեղինակի անունը, տպագրության ամսաթիվը և կվերադարձնի dict ներմուծած տվյալներով:

import argparse

def parsing():
    parser = argparse.ArgumentParser(prog = "Book", description = "Book info")
    parser.add_argument("--name", metavar = "Book name", type = str, required = True, help = "Book name")
    parser.add_argument("--author", metavar = "Author name", type = str, help = "Author name")
    parser.add_argument("--date", metavar = "Date", type = int, help = "Date")
    return parser.parse_args()

def main():
    arguments = parsing()
    book_info = {}
    book_info["name"] = arguments.name
    book_info["author"] = arguments.author
    book_info["date"] = arguments.date
    print(book_info)

main()

