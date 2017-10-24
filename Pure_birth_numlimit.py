import dendropy
import sys
import math
import collections
import itertools
from dendropy.calculate import probability
from dendropy.utility import GLOBAL_RNG
from dendropy.utility.error import TreeSimTotalExtinctionException
from dendropy.utility import constants
import random

def uniform_pure_birth_tree(birth_rate,rng=None):
    "Generates a uniform-rate pure-birth process tree. "
    if rng is None:
        rng = GLOBAL_RNG 
    tree = dendropy.Tree()
    tree.seed_node.edge.length = 0.0
    leaf_nodes = tree.leaf_nodes()
    total_length = 0.0
    while len(leaf_nodes)< 100.0: 
        waiting_time = rng.expovariate(len(leaf_nodes)*birth_rate)
        for nd in leaf_nodes:
            nd.edge.length += waiting_time
        parent_node = rng.choice(leaf_nodes)
        c1 = parent_node.new_child()
        c2 = parent_node.new_child()
        c1.edge.length = 0.0
        c2.edge.length = 0.0
        total_length += c1.distance_from_root()
        leaf_nodes = tree.leaf_nodes()
    leaf_nodes = tree.leaf_nodes()
    waiting_time = rng.expovariate(len(leaf_nodes)*birth_rate)
    for nd in leaf_nodes:
        nd.edge.length += waiting_time
    tree.is_rooted = True
    return tree

def main():
    data_file = open('pure_birth_treelength.csv', 'w')
    data_file.write('Speciation Rate, Length of Tree\n')
    birth_rate = 0.1

    while birth_rate <= 10:
       fname = "tree_"+str(birth_rate)+"_purebirth.tree.txt"
       ofile = open(fname,'w')
       t = uniform_pure_birth_tree(birth_rate)
       ofile.write(t.as_string(schema="nexus"))
       ofile.close()
       length = 0
       for node in t.leaf_node_iter():
           l = node.distance_from_root()
           length = max(l,length)
    
       data_file.write(str(birth_rate)+ ','+ str(length)+'\n')
       birth_rate += 0.1

    
    

