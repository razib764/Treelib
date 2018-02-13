import dendropy
import matplotlib.pyplot as plt


def node_graph():
    birth_rate = 0.001
    nodes = []
    rate = []
    while birth_rate < 0.01:
       t = dendropy.model.birthdeath.birth_death_tree(birth_rate,0.0,max_time=100)
       nodes += [len(t.leaf_nodes())]
       rate += [birth_rate]
       birth_rate += 0.001
    plt.plot(rate, nodes, 'b-')
    plt.axis([0.0,0.01, 0,10])
    plt.show()

def len_graph():
    birth_rate = 0.1
    length = []
    rate = []
    while birth_rate <= 1:
       t = dendropy.model.birthdeath.birth_death_tree(birth_rate,0.0,num_total_tips=100) 
       length += [(t.length())]
       rate += [birth_rate]    
       birth_rate += 0.1
    plt.plot(rate, length, 'b-')
    plt.axis([0.0,1.1, 0,2000])
    plt.show()
    
    
node_graph()
len_graph()