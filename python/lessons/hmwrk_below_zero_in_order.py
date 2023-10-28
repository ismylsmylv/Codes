mainlist = [-15, 15, 1, 23, -64, 76, -87, 45, 754, -2]
belows = []
while mainlist:
    min = mainlist[0]
    for x in mainlist:
        if x < min:
            min = x
    belows.append(min)
    mainlist.remove(min)
print(belows)