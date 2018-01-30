import pandas as pd
import dendropy
from dendropy.utility import GLOBAL_RNG
import math
import matplotlib.pyplot as plt

tree = dendropy.Tree()
tree.seed_node.edge.length = 0.0
def uniform_pure_birth_tree(birth_rate,rng=None):
    "Generates a uniform-rate pure-birth process tree."
    if rng is None:
        rng = GLOBAL_RNG 
    tree = dendropy.Tree()
    tree.seed_node.edge.length = 0.0
    leaf_nodes = tree.leaf_nodes()
    #total_length = 0.0
    while len(leaf_nodes) < 100.0: 
        waiting_time = rng.expovariate(len(leaf_nodes)*birth_rate)
        for nd in leaf_nodes:
            nd.edge.length += waiting_time
        parent_node = rng.choice(leaf_nodes)
        c1 = parent_node.new_child()
        c2 = parent_node.new_child()
        c1.edge.length = 0.0
        c2.edge.length = 0.0
        #total_length = c1.distance_from_root()
        leaf_nodes = tree.leaf_nodes()
    leaf_nodes = tree.leaf_nodes()
    waiting_time = rng.expovariate(len(leaf_nodes)*birth_rate)
    for nd in leaf_nodes:
        nd.edge.length += waiting_time
    tree.is_rooted = True
    return tree


def main():
    birth_rate = 0.01
    length = []
    rate = []
    while birth_rate <= 1:
       '''for i in range(1,10):
           rate_length = []
           t = uniform_pure_birth_tree(birth_rate)
           rate_length += [t.length()]'''
       t = uniform_pure_birth_tree(birth_rate)    
       length += [math.log(t.length())]
       #length += [math.log(sum(rate_length)/float(len(rate_length)))]
       rate += [birth_rate]    
       birth_rate += 0.1
    plt.plot(rate, length, 'b-')
    plt.axis([0.0,1.01, 4,10])
    plt.show()

main()    
"""
This graph should decrease exponentially.
As the birth rate increases, the time taken to reach a fixed number of nodes decreases,
therefore, the total time (or length) of the tree will decrease
The decrease is exponential because the waiting times are exponential functions
"""