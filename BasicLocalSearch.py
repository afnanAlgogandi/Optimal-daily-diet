def objectiveFunction(X, Y, Z):
    return (22 * X + 65 * Y + 18 * Z) + (420 * X + 280 * Y + 230 * Z)


def SetSolution(x, y, z, st):
    m = 4
    n = len(x)
    Set = []

    for i in range(st, len(x)):
        for j in range(st, len(y)):
            for k in range(st, len(z)):

                # constraint of  x, y, z greater than 0
                if x[i] >= 0 & y[j] >= 0 & z[k] >= 0:

                    # constraint of fat
                    if 35 * x[i] + 15 * y[j] + 16 * z[k] >= 60:

                        # constraint of carbohydrates
                        if 111 * x[i] + 100 * y[j] + 80 * z[k] >= 211:

                            # constraint of protein
                            if 25 * x[i] + 36 * y[j] + 16 * z[k] >= 85:

                                # constraint of sodium
                                if 0.085 * x[i] + 0.17 * y[j] + 0.98 * z[k] >= 2.3:
                                    OF = objectiveFunction(x[i], y[j], z[k])
                                    Set.append([x[i], y[j], z[k], OF])
    return Set


def initialSolution(Set, solutions):
    for i in range(len(solutions)):
        if i == 0:
            opt = solutions[0][3]
        else:
            opt = min(opt, solutions[i][3])

    for i in range(len(solutions)):
        if solutions[i][3] == opt:
            quantity = solutions[i]

    for i in range(len(Set)):
        if Set[i][3] == opt:
            index = i

    return quantity, index


def BasicLocalSearch(set, index, initsolution):
    s = initsolution
    a1 = []
    a2 = []
    r = 100
    optima = 99999999999

    for i in range(r):
        neighborhood1 = set[index + i]
        a1.append(neighborhood1)

        neighborhood2 = set[index - i]
        a2.append(neighborhood2)

    for j in range(len(a1)):
        minn = min(s[3], a1[j][3], a2[j][3])
        if (minn < optima):
            optima = minn
        else:
            optima = optima

    for k in range(len(set)):
        if (set[k][3] == optima):
            solution = set[k]
            index = k

    return index, solution


def cost(solution):
    return 22 * solution[0] + 65 * solution[1] + 18 * solution[2]


def calories(solution):
    return 420 * solution[0] + 280 * solution[1] + 230 * solution[2]


def neighborhood(index, solution, prvsolution):

    if solution == prvsolution:
        return solution
    else:
        prvsolution = solution
        index, solution = BasicLocalSearch(set, index, solution)

        print("\nNeighborhood: ", prvsolution[0], "dishes of burger,", prvsolution[1], "Salmon, and",
              prvsolution[2],
              "chicken ceasar salad")
        print("All meal will cost you", cost(prvsolution), "SR, and contains only", calories(prvsolution), "calories")
        print("Objective Function =",prvsolution[3])

        return neighborhood(index, solution, prvsolution)


x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
z = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
set = SetSolution(x, y, z, 0)

x = [1, 2, 3, 4]
y = [0, 1, 2, 5]
z = [0, 1, 2, 5]
initsolution, index1 = initialSolution(set, SetSolution(x, y, z, 0))
print("\nInitial Solution: ", initsolution[0], "dishes of burger,", initsolution[1], "Salmon, and", initsolution[2],
      "chicken ceasar salad")
print("All meal will cost you" , cost(initsolution) , "SR, and contains only", calories(initsolution),"calories")
print("Objective Function =",initsolution[3])

# neighborhoods :
index2, solution = BasicLocalSearch(set, index1, initsolution)
optimal = neighborhood(index2, solution, initsolution)

print("\n--------------------------------------------------------------------------------")
print("\nThe best diet is that it contains", optimal[0], "dishes of burger,", optimal[1], "Salmon, and", optimal[2],
      "chicken ceasar salad")
print("All meal will cost you" , cost(optimal) , "SR, and contains only", calories(optimal),"calories")
