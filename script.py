import getarguments
import json
import re

def first_substring(*args) -> dict:
    try:
        with open (args[0], "r") as cfile:
            lines = cfile.read().split("\n")
            new_lines = {}
            for i, line in enumerate(lines):
                if line.startswith(" ") and line.strip() != '':
                    if not lines[i-1].startswith(" "):
                        tmp = lines[i-1]
                        new_lines[tmp] = [] 
                    for j in args[1]:
                        if j in line:
                            new_lines[tmp].append(line)
            return new_lines
    except Exception as err:
        exit(err)

def second_substring(*args):
    new_dict = {}
    for key, value in args[1].items():
        new_dict[key] = {} 
        for line in value:
            for i in args[2]:
                if line.find(i) != -1:
                    try:
                        arg = float(re.findall(""r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)", line)[0])
                        arg_name = f"{line[line.find(i):line.find(i)+len(i)]}"
                        new_dict[key][arg_name] = arg
                    except:
                        with open (f"{args[0].stem}.anomaly", "a") as anom_file:
                            anom_file.write(f"{key}\n")
                            anom_file.write(f" {line}\n")
    return new_dict

def substring(*args):
    res_dict = {}
    new_dict = json.dumps(args[0], indent = 2)
    with open(f"{args[1].stem}.report", "w") as outfile:
        outfile.write(new_dict)
    for i in args[2]:
        res_dict[i] = []
        for value in args[0].values():
            if i in value:
                res_dict[i].append(value[i])
    result = {}
    for key, value in res_dict.items():
        dir_name = str(args[1].parent)
        result[dir_name] = {}
        result[dir_name][key] = {}
        if len(value) != 0:
            result[dir_name][key]["min"] = min(value)
            result[dir_name][key]["max"] = max(value)
            result[dir_name][key]["avg"] = sum(value)/len(value)
        result_dict = json.dumps(result, indent  = 2)
        with open(f"all_report.md", "a") as res_file:
            res_file.write(result_dict)
            res_file.write('\n')

def main():
    args = getarguments.get_arguments()
    for i in getarguments.get_files(args["report_dir"], args["file_patern"], args["file_extention"]):
        res = second_substring(i, first_substring(i, args["regexp"]), args["regexp"])
        substring(res, i, args["regexp"])

if __name__ == "__main__":
    main()
