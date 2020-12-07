def day2():
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

        numberonelist.append(int(x[0:dashlocation]))
        numbertwolist.append(int(x[dashlocation + 1:colonlocation - 2]))
        letterlist.append(x[colonlocation - 1])
        passlist.append(x[colonlocation + 2:len(x)])

    i = 0
    for x in passlist:

        if passlist[i].count(letterlist[i]) >= numberonelist[i] and passlist[i].count(letterlist[i]) <= numbertwolist[i]:
            valid += 1
        
        i += 1

    print(valid)

    f.close()


day2()
