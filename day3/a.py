def signf(val): # 0=>-1, 1=>1
    return 1 if val else -1

with open("input", "r") as file:

    lines = file.read().split("\n")

    size = len(lines[0])

    counter = [0 for x in range(size)]

    gammas = counter.copy() # most common values
    epsilons = counter.copy() # least common values

    for line in lines:
        for j,digit in enumerate(line):
            counter[j] += signf(bool(int(digit)))
    
    for i in range(size):
        gammas[i] = 1 if counter[i] > 0 else 0
        epsilons[i] = 1 if counter[i] < 0 else 0

    gamma = int(''.join(map(str,gammas)), base=2)
    epsilon = int(''.join(map(str,epsilons)), base=2)
            
    print ("gamma:", gamma,"epsilon:", epsilon,"product:", gamma * epsilon)