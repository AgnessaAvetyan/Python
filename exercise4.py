#Օգտ ա տ իրոջից ստ ա նա լ եռա նկյա ն 2 էջերը, հա շվել ներքնա ձիգը և տ պ ել

import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > 0 and b > 0:
    print("Triangle rifle is:", round(math.sqrt(a**2 + b**2),2))
else:
    print("Invalid first or second number")
