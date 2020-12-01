def day1():
    f = open("./day1input.txt", "r")

    numbers = []

    for x in f:
        numbers.append(int(x))

    for x in numbers:
        for y in numbers:
            if x + y == 2020:
                print(x * y)
                return

    f.close()

day1()
