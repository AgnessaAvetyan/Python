#Առա ջին set-ից հեռա ցնել ա յն էլեմենտ ները որոնք կա ն երկրորդում

Set1 = {10, 20, 7, 36, 30}
Set2 = {20, 36, 40, 3, 50}

Set3 = Set1.intersection(Set2)
Set1 = Set1.difference(Set3)
print(f"Set1 is {Set1}")
