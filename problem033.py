import helper

product = 1
for i in range(11, 100):
    for j in range(i+1, 100):
        f1 = i / j

        dI = helper.getAllDigitsOfNumber(i)
        dJ = helper.getAllDigitsOfNumber(j)

        if dI[1] == 0 or dJ[1] == 0:
            continue

        f2 = 0
        if dI[0] == dJ[1]:
            f2 = dI[1] / dJ[0]
        elif dI[1] == dJ[0]:
            f2 = dI[0] / dJ[1]
        elif dI[1] == dJ[1]:
            f2 = dI[0] / dJ[0]
        elif dI[0] == dJ[0]:
            f2 = dI[1] / dJ[1]

        if f1 == f2:
            product *= (j / i)
        
print(product)