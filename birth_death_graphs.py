import pandas as pd
import dendropy

"""
The follwong code implements the uniform birth death tree model of dendropy for different ratios of 
birth rate and death rate
The ratio starts at 1:1 and increases by 1 in each step
Every tree grows upto 100 nodes 
A graph of the number of nodes of a tree v/s the total length of the tree at different birth rates is produced. 
"""
def ratio_test():
    birth_rate = 0.1
    death_rate = 0.1
    length = []
    nodes = []
    while birth_rate <= 10:
       t = dendropy.model.birthdeath.birth_death_tree(birth_rate,death_rate,num_total_tips=100)
       nodes += [len(t.leaf_nodes())]
       length += [t.length()]
       birth_rate += 0.1
    df = pd.DataFrame(nodes,length, columns=["Length"])
    df.plot()
    
