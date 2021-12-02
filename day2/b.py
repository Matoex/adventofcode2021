with open("input", "r") as file:

    values = file.read()
    values = values.split("\n")

    x, y, aim = 0, 0, 0

    for e in values:
        e = e.split(" ")
        cmd = e[0]
        num = int(e[1])

        if cmd == "forward":
            x += int(num)
            y += aim * num
        if cmd == "down":
            aim += int(num)
        if cmd == "up":
            aim -= int(num)
        else:
            print(e)

    print("x", x, "y", y, "x*y", x*y)