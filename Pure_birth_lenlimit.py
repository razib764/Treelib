import dendropy
from dendropy.utility import GLOBAL_RNG

def uniform_pure_birth_tree(birth_rate,rng=None):
    "Generates a uniform-rate pure-birth process tree. "
    if rng is None:
        rng = GLOBAL_RNG 
    tree = dendropy.Tree()
    tree.seed_node.edge.length = 0.0
    leaf_nodes = tree.leaf_nodes()
    total_length = 0.0
    while total_length< 100.0: 
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

def main():
    data_file = open('pure_birth_numspecies.csv', 'w')
    data_file.write('Speciation Rate, Number of Leaves\n')
    birth_rate = 0.1

    while birth_rate <= 10:
       fname = "tree_"+str(birth_rate)+"_purebirth.tree.txt"
       ofile = open(fname,'w')
       t = uniform_pure_birth_tree(birth_rate)
       ofile.write(t.as_string(schema="nexus"))
       ofile.close()
       nodes = len(t.leaf_nodes())
       data_file.write(str(birth_rate)+ ','+ str(nodes)+'\n')
       birth_rate += 0.1

    
    

