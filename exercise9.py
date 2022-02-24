#Գրել ծրա գիր, որը կհա շվի ներմուծա ծ ինթեջերի թվա նշա նների քա նա կը։ օրինա կ՝ 3489 ֊ի դեպ քում պ ետ ք է տ պ ի 4

number = int(input("Please enter the number: "))

count = 0
if number < 0:
    number *= -1
if number == 0:
    print("Number of digit is 1")
else:
    while number > 0:
        count += 1
        number //= 10
    print("Number of digits is", count)
