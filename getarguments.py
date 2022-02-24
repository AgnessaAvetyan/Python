import argparse
import json
from pathlib import Path

def parser():
    parser = argparse.ArgumentParser(prog = "Search", description = "Search words in files")
    parser.add_argument("--config_file",metavar = "Config File", type = str, help = "Config file json format") 
    parser.add_argument("--report_dir", metavar = "Path directory", type = str, help = "Directory's path")
    parser.add_argument("--regexp", metavar = "Words", nargs = "+", help = "Words, which must find")
    parser.add_argument("--file_patern", metavar = "Path file", type = str, help = "File's path")
    parser.add_argument("--file_extention", metavar = "Extention", type = str, help = "Extention file, which must find")
    return parser.parse_args()
    
def get_files(dir_path, file_path, file_ex, files_list = []):
    try:
        for path in Path(dir_path).iterdir():
            if path.is_dir():
                get_files(path, file_path, file_ex)
            elif file_path in path.stem and path.name.endswith(file_ex):
                files_list.append(path)
        return files_list
    except Exception as e:
        exit(f"{e}") 

def get_cfile_arguments(cfile):
    try:
        cfile.endswith(".json")
        with open (cfile, "r") as conf_file:
            return json.load(conf_file)
    except Exception as err:
        exit(f"Config file error: {err}")

def check_args(args: dict) -> dict:
    if args["report_dir"] == None:
        args["report_dir"] = "."
    if args["file_extention"] == None:
        args["file_extention"] = ""
    if args["file_patern"] == None:
        args["file_patern"] = ""
    return args

def get_arguments() -> dict:
    args = {} 
    if parser().config_file and parser().regexp == parser().report_dir == parser().file_patern == parser().file_extention == None:
        args = get_cfile_arguments(parser().config_file)
    elif not parser().config_file and parser().regexp:
        args["regexp"] = parser().regexp
        args["report_dir"] = parser().report_dir
        args["file_extention"] = parser().file_extention
        args["file_patern"] = parser().file_patern
    else:
        exit(f"Please, input only config file or file regexp, that is required")
    return check_args(args)
