import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker


#define a main
def main():
    # create a random list of floats following a uniform distribution
    # draw a poisson distribution with parameter lambda = 1
    # draw a poisson distribution with parameter lambda = 2
    # draw a poisson distribution with parameter lambda = 3
    # draw a poisson distribution with parameter lambda = 4
    l = np.random.poisson(0., 10000)
    print(l)


    # plot the data in l_0 in percentage
    # sum up each equal element in l_0
    l_0 = 0
    l_1 = 0
    for i in l:
        if i == 0:
            l_0 += 1
        else:
            l_1 += 1

    # make percentages
    l_0 = l_0 / len(l)
    l_1 = l_1 / len(l)

    print(l_0)
    print(l_1)

    # plot the data
    plt.bar([0, 1], [l_0, l_1], color=['blue', 'orange'])


    plt.title('Poisson Distributions')
    plt.show()

if __name__ == '__main__':
    main()

