import pandas as pd
import dendropy
from dendropy.utility import GLOBAL_RNG

def uniform_pure_birth_tree(birth_rate, rng=None):
    "Generates a uniform-rate pure-birth process tree. "
    if rng is None:
        rng = GLOBAL_RNG 
    tree = dendropy.Tree()
    tree.seed_node.edge.length = 0.0
    leaf_nodes = tree.leaf_nodes()
    total_length = 0.0
    while total_length < 100.0: 
        waiting_time = rng.expovariate(len(leaf_nodes)*birth_rate)
        for nd in leaf_nodes:
            nd.edge.length += waiting_time
        parent_node = rng.choice(leaf_nodes)
        c1 = parent_node.new_child()
        c2 = parent_node.new_child()
        c1.edge.length = 0.0
        c2.edge.length = 0.0
        total_length = c1.distance_from_root()
        leaf_nodes = tree.leaf_nodes()
    leaf_nodes = tree.leaf_nodes()
    waiting_time = rng.expovariate(len(leaf_nodes)*birth_rate)
    for nd in leaf_nodes:
        nd.edge.length += waiting_time
    tree.is_rooted = True
    return tree

uniform_pure_birth_tree(0.001).print_plot()


def main():
    birth_rate = 0.01
    nodes = []
    rate = []
    while birth_rate < 0.1:
       t = uniform_pure_birth_tree(birth_rate)
       nodes += [len(t.leaf_nodes())]
       rate += [birth_rate]
       birth_rate += 0.01
    df = pd.DataFrame(nodes,rate)
    print(df)
    df.plot() 
    
