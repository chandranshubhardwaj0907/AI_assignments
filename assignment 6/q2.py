def fitness(bag, bits, capacity):
    fit = []
    f_list = []
    n = len(bag)

    for i in range(n):
        f_value = 0
        f_weight = 0
        for j in range(len(bits[i])):
            if bits[i][j] == 1:
                f_weight += bag[j][1]
                f_value += bag[j][2]
        if f_weight <= capacity:
            fit.append(bits[i])
            f_list.append(f_value)
        else:
            f_value = 0
            fit.append(bits[i])
            f_list.append(f_value)
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(f_list) - 1):
            if f_list[i] < f_list[i + 1]:
                f_list[i], f_list[i + 1] = f_list[i + 1], f_list[i]
                fit[i], fit[i + 1] = fit[i + 1], fit[i]
                swapped = True

    return fit, f_list

def crossover(fit):
        fit[2][2], fit[3][2] = fit[3][2], fit[2][2]
        fit[2][3], fit[3][3] = fit[3][3], fit[2][3]
        return fit


def mutation(fit, iteration):
    cycle = [2, 0, 3, 1]
    counter = cycle[(iteration % 4)]
    if fit[2][counter]==0:
        fit[2][counter]=1
    else:
        fit[2][counter]=0
    return fit



def genetic_algorithm(bag, bits, capacity):
    iterations=4
    for iteration in range(iterations):
        fit,f_list = fitness(bag, bits, capacity)
        fit=crossover(fit)
        fit=mutation(fit, iteration)
        bits=fit
    fit, f_list = fitness(bag, bits, capacity)
    return fit, f_list

def main():
    bag = [['A', 2, 3], ['B', 3, 5], ['C', 4, 7], ['D', 5, 9]]
    bits = [[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1]]
    capacity = 9
    fit,f_list = genetic_algorithm(bag, bits, capacity)
    print("Fit items after 4 iterations:",fit[0])
    print("Fittest cromosome:",max(f_list))
main()