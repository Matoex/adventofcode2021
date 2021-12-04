def heaviside(val, zeroval): # 0000 zeroval 11111
    return zeroval if val == 0 else 1 if val > 0 else 0


def r2li(s): # contert right side index to left side index, depending on the size
    global size
    return size - s - 1


def signf(val): # 0=>-1, 1=>1
    return 1 if val else -1


def count(list, s): # counts the 0,1 at s in the list
    counter = 0
    for line in list:
        counter += signf(1 << r2li(s) & line != 0)
    return counter


def match(set, s, zeroval): #filter set
    return [line for line in set if (1 << r2li(s)) & line == (heaviside(counter, zeroval) << r2li(s))]


with open("input", "r") as file:

    lines_org = file.read().split("\n")
    oxygen = list(map(lambda x: int(x, base=2), lines_org))

    size = len(lines_org[0])

    co2 = oxygen.copy()

    for s in range(size):
        if(len(oxygen) > 1):
            counter = count(oxygen, s)
            oxygen = match(oxygen, s, 1)

        if(len(co2) > 1):
            counter = -count(co2, s)
            co2 = match(co2, s, 0)

    oxygen,co2 = oxygen[0],co2[0]

    print("oxygen", oxygen, "co2", co2, "product", oxygen * co2)
