def day1():
    f = open("./day1input.txt", "r")

    numbers = []

    for x in f:
        numbers.append(int(x))

    for x in numbers:
        for y in numbers:
            for z in numbers:
                if x + y + z == 2020:
                    print(x * y * z)
                    return

    f.close()

day1()