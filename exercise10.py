#Գրել ծրա գիր, որը կհա շվի ներմուծա ծ թվի ֆա կտ որիա լը:

number = int(input("Enter the number: "))

if number == 0:
    print("Factorial is 1")
elif number > 0:
    res = i = 1
    while i <= number:
        res *= i
        i += 1
    print("Factorial is", res)
else:
    print("Invalid number!")
