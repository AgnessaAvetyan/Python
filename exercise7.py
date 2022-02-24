#Գրել ծրա գիր, որը 2 լիստ երից կստ եղծի 3֊րդ լիստ ը՝ 1֊ին լիստ ից վերցնելով կենտ ինդեքսի ա րժեքները և 2֊րդ լիստ ից զույգ ինդեքսի ա րժեքները
    

list_1 = [1,2,3,4,5,6]
list_2 = ['a','b','c','d']
list_3 = []

for i in range(len(list_1)):
    if i % 2 == 1:
        list_3.extend([list_1[i]])
for i in range(len(list_2)):
    if i % 2 == 0:
        list_3.extend([list_2[i]])

print(list_3)
