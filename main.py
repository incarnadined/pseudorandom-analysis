import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import itertools

def random(x, k, c, m):
    return (k * x + c ) % m

if __name__ == '__main__':
    seed = 53
    tests = 100 # number of random numbers to generate for testing
    variable_variable = 0 # which variable will be plotted against chi? (k->0, c->1, m->2)
    
    k = np.arange(1, 10, 1)
    c = np.arange(1, 10, 1)
    m = np.arange(1, 10, 1)
    random_number_bins = np.zeros(m.shape)
    chis = [[], [], [], []] # [k, c, m, chi_square]
    averaged_chis = [[], [], [], []] 

    for x in itertools.product(k, c, m):
        random_number_bins = np.zeros(m.shape)
        while np.sum(random_number_bins) < tests:
            seed = random(seed, *x)
            random_number_bins[seed] += 1
        
        chis[0].append(x[0])
        chis[1].append(x[1])
        chis[2].append(x[2])
        chis[3].append(stats.chisquare(random_number_bins)[1])
    
    constant_variables = [0, 1, 2].remove(variable_variable)
    # find average chi values for a specific variable (k/c/m)
    for constant in constant_variables:
        constant_values = set(chis[constant])
        averages = {constant_value: sum([chis[3][i] for i in range(chis[constant]) if chis[constant][i] == constant_value]) for constant_value in constant_values}
        averaged_chis[constant] = averages.keys()
        averaged_chis[3] = averages.values()



    plt.plot([chis[0][i]*chis[1][i]*chis[2][i] for i in range(len(chis[3]))], chis[3], '-ro')
    plt.xlabel('Product of k, c, m')
    plt.ylabel('Chi-Squared Value')
    plt.show()