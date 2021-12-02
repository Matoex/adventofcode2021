with open("input", "r") as file:

    values = file.read()
    values = list(map(lambda x: int(x), values.split("\n")))

    # zip with offset one, compare tupels, filter trues and count them
    print(
        len(
            list(
                filter(
                    lambda a: a,
                    list(
                        map(lambda a: a[0] < a[1],
                            list(
                                zip(values, values[1:]))))))))
