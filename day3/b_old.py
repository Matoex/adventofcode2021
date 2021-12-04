with open("input", "r") as file:

    lines_org = file.read().split("\n")

    size = len(lines_org[0])

    oxygen = lines_org.copy()
    co2 = lines_org.copy()

    for s in range(size):
        if(len(oxygen) > 1):
            counter = 0

            for line in oxygen:
                if(bool(int(line[s]))):
                    counter += 1
                else:
                    counter -= 1
            character = "0" if counter < 0 else "1"
            oxygen = [line for line in oxygen if line[s] == character]

        if(len(co2) > 1):

            counter = 0

            for line in co2:
                if(bool(int(line[s]))):
                    counter += 1
                else:
                    counter -= 1

            character = "1" if counter < 0 else "0"
            co2 = [line for line in co2 if line[s] == character]

    oxygen = int(oxygen[0], base=2)
    co2 = int(co2[0], base=2)

    print("oxygen", oxygen, "co2", co2, "product", oxygen * co2)
