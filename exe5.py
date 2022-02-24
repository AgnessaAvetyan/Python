#Գրել ֆունկցիա, որը ա րգումենտ ում կստ ա նա  integer, կբա զմա պ ա տ կի տ րվա ծ թվի թվա նշա նները իրա ր ա յնքա ն ժա մա նա կ, քա նի դեռ ա րդյունքը չի ստ ա ցվել միա նիշ թիվ։ Վերա դարձնել ստ ա ցված ա րդյունքը և տ պ ել։

def digits_mul(n):
    try:
        int(n)
    except:
        return digits_mul(input("Please enter only number: "))
    n = int(n)
    res = 1
    while n != 0:
        res *= n % 10
        n //= 10
    if res > 9:
        return digits_mul(res)
    return res

print(digits_mul(input("Please, enter integer: ")))
