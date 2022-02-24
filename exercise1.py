#Գրել ծրա գիր, որը կունենա  3 հա տ  string փ ոփ ոխ ա կա ն հետ ևյա լ ա րժեքներով՝ apple, little, mule։
#Ստ ա նա լ multiple բա ռը՝ օգտ ա գործելով slice մեթոդը և միա ցնելով 3 բա ռերի մա սերը։

part_1 = "apple"
part_2 = "little"
part_3 = "mule"

print(part_3[:3] + part_2[2::4] + part_2[1::5] + part_1[2:])
