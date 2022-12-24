
import random
from numpy import exp
import warnings
from numpy.random import rand


def objectiveFunction(X, Y, Z):
    return (22 * X + 65 * Y + 18 * Z) + (420 * X + 280 * Y + 230 * Z)

def SetSolution(x, y, z):
    set_solutions = []

    for i in range(len(x)):
        for j in range(len(y)):
            for k in range(len(z)):
                if x[i] >= 0 and y[j] >= 0 and z[k] >= 0:  # const domain grater than zero
                    if 35 * x[i] + 15 * y[j] + 16 * z[k] >= 60:  # const of fat
                        if 111 * x[i] + 100 * y[j] + 80 * z[k] >= 211:  # const of carbohydrates
                            if 25 * x[i] + 36 * y[j] + 16 * z[k] >= 85:  # const of protein
                                if 0.085 * x[i] + 0.17 * y[j] + 0.98 * z[k] >= 2.3:  # const of sodium
                                    objective = objectiveFunction(x[i], y[j], z[k])
                                    set_solutions.append([x[i], y[j], z[k], objective])
    return set_solutions


def simulated_annealing(set, initial, n_iterations=100, step_size= 0.1, temp=10):
    candidate = set.index(initial)
    # initial point
    best = initial
    print("\ninitial solution : ")
    toString(best)
    # evaluate the initial point
    best_eval = objectiveFunction(best[0], best[1], best[2])

    curr, curr_eval = best, best_eval

    for i in range(n_iterations):
        # Take a step for the better
        candidate = int(candidate + random.randint(0, (len(set)-1)) * step_size) % len(set)
        # evaluate candidate
        candidate_eval = objectiveFunction(set[candidate][0], set[candidate][1], set[candidate][2])

        # check for new best solution
        if candidate_eval < best_eval:
            # store new best point
            best, best_eval = candidate, candidate_eval
            print("\nnew best point in simulated annealing method : ")
            toString(find(best_eval, set))

        diff = candidate_eval - curr_eval
        t = temp / float(i + 1)
        warnings.filterwarnings('ignore')
        metropolis = exp(-diff / t)

        # check if we should keep the new point
        if diff < 0 or rand() < metropolis:
            # store the new current point
            curr, curr_eval = candidate, candidate_eval

    return best_eval


def find(best_eval, set):

    # find element of optimal solution
    for i in range(len(set)):
        if (set[i][3] == best_eval):
            return set[i]

    return "NULL"


def toString(solution, flag = False):
    cost = (22 * solution[0] + 65 * solution[1] + 18 * solution[2])
    calories = (420 * solution[0] + 280 * solution[1] + 230 * solution[2])

    if(flag):
        print("\nThe best diet is that it contains", solution[0], "dishes of burger,", solution[1], "Salmon, and",
              solution[2],"chicken ceasar salad")
        print("All meal will cost you", cost, "SR, and contains only", calories, "calories")
    else:
        print(solution[0], "dishes of burger,", solution[1], "Salmon, and", solution[2], "chicken ceasar salad")
        print("All meals will cost you", cost, "SR, and contains only", calories, "calories")
        print("objective Function", solution[3])


random.seed(2)

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # quantity of burger meals
y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # quantity of slamon meals
z = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # quantity of ceaser salad meals

set = SetSolution(x, y, z)  # possible solutions
best_eval = simulated_annealing(set, set[random.randint(0,len(set)-1)])  # best solution with simulated annealing algorithm
solution = find(best_eval, set)  # best quantity of meals

print("\n_______________________________________________________")
toString(solution, True)
