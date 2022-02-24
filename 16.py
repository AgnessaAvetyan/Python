#!/usr/bin/python3

#Գրել ծրա գիր, որը որպ ես ա րգումենտ կստ ա նա  directory, որը ունի նա և subdirectory-ներ և կտ պ ի բոլոր ֆա յլերի ա նունները․

import argparse
from pathlib import Path

def parsing():
    parser = argparse.ArgumentParser(prog = "Path", description = "All files in directory")
    parser.add_argument("--path", metavar = "Full Path", type = str, help = "Full path a directory")
    return parser.parse_args()

def get_files(path_dir):
    for path in Path(path_dir).iterdir():
        if path.is_dir():
            get_files(path)
        else:
            print(path.name)

def main():
    get_files(parsing().path)

if __name__ == "__main__":
    main()
