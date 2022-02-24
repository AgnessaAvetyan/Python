#Տրվա ծ tuple-ում ներա ռվա ծ list-ի 2֊րդ էլեմենտ ը փ ոխ ա րինելtuple-ի 3֊րդ էլեմենտ ով

Tuple1 = (11, [22, 3, 33, 7], 44, 55, 105)
print(f"Initial tuple: {Tuple1}")

Tuple1[1][2] = Tuple1[3]
print(f"Changed tuple: {Tuple1}")
