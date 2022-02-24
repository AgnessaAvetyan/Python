#Գրել ծրա գիր որը կհեռա ցնի նոր տ ողի սիմվոլները ֆա յլից եւ կտ պ ի։

with open("text.txt","r") as text:
    result = text.readlines()
print(f"Start:\n{result}\n")
result_str = " ".join(result)
for i in result_str:
    i = i.replace('\n',"")
print(f"End:\n{result_str}")
