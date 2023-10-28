#place numbers by ascending order in list
mainlist = [-15, 15, 1, 23, -64, 76]
copied = []
while mainlist:
    min = mainlist[0]
    for x in mainlist:
        if x < min:
            min = x
    copied.append(min)
    mainlist.remove(min)
print(copied)