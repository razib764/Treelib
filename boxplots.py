"""
The following method creates boxplots of the variance of data for the number of
nodes for 10 different birthrates with fixed maximum time over 100 iterations
per birth rate
"""
import dendropy
import matplotlib.pyplot as plt
from ete3 import Tree, TreeStyle

def box_plot():
    birth_rate = 0.2 #initial vaue
    death_rate = 0.1
    rate = [] #list of rates will be populated
    plot = [] #list of a list of variances will be populated
    while birth_rate < 1:
        birth_rate = round(birth_rate,1)
        death_rate = round(death_rate,1)
        rate += [birth_rate]
        i = 0
        num_avg = [] #list of number of nodes at a given birth rate for 100 iterations
        while i<2000:
            t = dendropy.model.birthdeath.birth_death_tree(birth_rate,death_rate,max_time=5)
            num_avg += [len(t.leaf_nodes())]
            i += 1
        plot += [[num_avg]]
        birth_rate += 0.1
        death_rate += 0.1
    plt.boxplot(plot)
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],rate)
    plt.show()
    
box_plot()

#variance mathematically 
#