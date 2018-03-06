import dendropy
import matplotlib.pyplot as plt
import math


def node_graph():
    birth_rate = 0.01
    nodes = []
    rate = []
    while birth_rate < 1:
       i = 0
       length_avg = 0
       while i<100:
           t = dendropy.model.birthdeath.birth_death_tree(birth_rate,0.0,max_time=5)
           length_avg += len(t.leaf_nodes())
           i += 1
       nodes += [math.log(length_avg/100)]
       rate += [birth_rate]
       birth_rate += 0.01
    plt.plot(rate, nodes, 'b-')
    plt.axis([0.0,1.1, 0,10])
    plt.show()



def len_graph():
    birth_rate = 0.01
    length = []
    rate = []
    while birth_rate <= 1:
       i = 0
       node_avg = 0
       while i<100:
           t = dendropy.model.birthdeath.birth_death_tree(birth_rate,0.0,num_total_tips=10) 
           node_avg += t.length()
           i += 1
       length += [node_avg/100]
       rate += [1/birth_rate]    
       birth_rate += 0.01
    plt.plot(rate, length, 'b-')
    plt.axis([0,101, 0,1000])
    plt.show()
    
    
#node_graph()
len_graph()