def day2p2():
    f = open("./day2input.txt", "r")

    lines = []
    colonlocation = 0
    numberonelist = []
    numbertwolist = []
    letterlist = []
    passlist = []
    dashlocation = 0
    valid = 0

    for x in f:
        lines.append(x)

    for x in lines:
        colonlocation = x.index(':')
        dashlocation = x.index('-')

        numberonelist.append(int(x[0:dashlocation]) - 1)
        numbertwolist.append(int(x[dashlocation + 1:colonlocation - 2]) - 1)
        letterlist.append(x[colonlocation - 1])
        passlist.append(x[colonlocation + 2:len(x)])

    i = 0

    for x in passlist:
        
        positions = 0

        if passlist[i][numberonelist[i]] == letterlist[i]:
            positions += 1
        
        if passlist[i][numbertwolist[i]] == letterlist[i]:
            positions += 1

        if positions == 1:
            valid +=1
        
        i += 1

    print(valid)

    f.close()


day2p2()