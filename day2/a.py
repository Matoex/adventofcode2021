with open("input", "r") as file:

    values = file.read()
    values = values.split("\n")

    x, y = 0, 0

    for e in values:
        e = e.split(" ")
        if e[0] == "forward":
            x += int(e[1])
        if e[0] == "down":
            y += int(e[1])
        if e[0] == "up":
            y -= int(e[1])
        else:
            print(e)

    print("x", x, "y", y, "x*y", x * y)