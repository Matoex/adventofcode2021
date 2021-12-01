with open("1.csv", "r") as file:

    values = file.read()
    values = values.split("\n")

    drag = None
    counter = 0
    for x in values:
        x = int(x)
        if drag != None:
            if x > drag:
                counter+=1
        drag = x

    print(counter)