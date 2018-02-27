import dendropy
import matplotlib.pyplot as plt

def box_plot():
    birth_rate = 0.1
    rate = []
    l = []
    while birth_rate < 1:
        print(birth_rate)
        rate += [(birth_rate//0.1)/10]
        i = 0
        length_avg = []
        while i<100:
            t = dendropy.model.birthdeath.birth_death_tree(birth_rate,0.0,max_time=5)
            length_avg += [len(t.leaf_nodes())]
            i += 1
        l += [[length_avg]]
        birth_rate += 0.1
    plt.boxplot(l)
    plt.xticks([1,2,3,4,5,6,7,8,9,10],rate)
    plt.show()
   
        
box_plot()

