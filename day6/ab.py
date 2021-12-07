def day_passed(number_of_ages):
    newborns = 0
    for (age, number) in enumerate(number_of_ages):
        if age == 0:
            newborns = number_of_ages[0]
            number_of_ages[0] = 0
        else:
            number_of_ages[age - 1] = number
    number_of_ages[8] = newborns
    number_of_ages[6] += newborns
    return number_of_ages


maxAge = 9

with open("input", "r") as file:

    ages = map(int, file.read().split(","))

    number_of_ages = [0]*maxAge

    for age in ages:
        number_of_ages[age] += 1

    for i in range(80):
        # print(i, number_of_ages, sum(number_of_ages))
        number_of_ages = day_passed(number_of_ages)

    print(f'a: {sum(number_of_ages)}')

    for i in range(256-80):
        # print(i, number_of_ages, sum(number_of_ages))
        number_of_ages = day_passed(number_of_ages)

    print(f'b: {sum(number_of_ages)}')
