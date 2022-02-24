#/usr/bin/python3

#Slice list into 3 equal chunks and reverse each chunk 
#sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89] (edited) 

def list_reverse(my_list):
    if len(my_list) % 3 != 0:
        return "Your list don't slice to 3 equal chunks"
    res_list = []
    i = 0
    while i < len(my_list):
        res_list.append(my_list[i:i+3][::-1])    
        i += 3 
    return res_list

def main():
    sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    print(f"Your list is: {sample_list}\nYour reverse list is: {list_reverse(sample_list)}")

if __name__ == "__main__":
    main()
