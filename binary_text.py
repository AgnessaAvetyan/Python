#/usr/bin/python3

def binary_to_decimal(byn_txt):
    byn_list = []
    res = ""
    i = 0
    if len(byn_txt) % 8 != 0:
        return "Invalid text"
    while i < len(byn_txt):
        byn_list.append(byn_txt[i:i + 8])
        i += 8 
    for i in byn_list:
        res += chr(bynary_converter_to_decimal(i))
    return res

def bynary_converter_to_decimal(byn):
    result = 0
    for i in range(8):
        result += int(byn[7 - i]) * 2 ** i
    return result

def main():
    with open ("binary_text.txt", 'r') as f_bin: 
        binary_text = f_bin.readline().strip("\n")
    print(binary_to_decimal(binary_text))

if __name__ == "__main__":
    main()
