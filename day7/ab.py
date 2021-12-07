with open("input", "r") as file:

    values = file.read().split(",")
    values = [int(x) for x in values]

    coasts_a = []
    coasts_b = []
    for position in range(min(values), max(values)+1):

        distance_a, distance_b = 0, 0

        for x in values:
            current_distance = abs(position - x)
            distance_a += current_distance
            distance_b += (current_distance * (current_distance+1))/2
        coasts_a.append(distance_a)
        coasts_b.append(distance_b)

    coasts_a.sort()
    coasts_b.sort()

    print(f'distance_a: {coasts_a[0]}')
    print(f'distance_b: {coasts_b[0]}')
