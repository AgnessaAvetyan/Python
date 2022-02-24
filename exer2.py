#Write a Python program to create a list reflecting the modified run-length encoding from a given list of integers or a given list of characters. 
#
#Original list:
#
#[1, 1, 2, 3, 4, 4, 5, 1]
#
#List reflecting the modified run-length encoding from the said list:
#
#[[2, 1], 2, 3, [2, 4], 5, 1]
#
#Original String:
#
#aabcddddadnss
#
#List reflecting the modified run-length encoding from the said string:
#
#[[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]

in_list = []
n = input("input list member! ")
while n:
	if n.isnumeric():
		in_list.append(int(n))
	else:
		in_list.append(n) 
	n = input("input list member! ")
i = 0
count = 1
out_list = []
while i <= len(in_list) - 1:
    j = i
    tmp = in_list[i]
    while j < len(in_list) - 1:
        if in_list[j] == in_list[j + 1]:
            count += 1
            j += 1
        else:
            break
    if count > 1:
        out_list.append([count, tmp])
    else:
        out_list.append(tmp)
    i = j + 1
    count = 1
print(out_list)
