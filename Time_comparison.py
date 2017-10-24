import sys
import math
import random
import collections
import itertools
from dendropy.calculate import probability
from dendropy.utility import GLOBAL_RNG
from dendropy.utility.error import TreeSimTotalExtinctionException
from dendropy.utility import constants
import dendropy
import time

speciation = 1.0 #all speciations occur at rate of 1.0

"""
iterative model from https://pythonhosted.org/DendroPy/_modules/dendropy/model/birthdeath.html#birth_death_tree
"""
def uniform_pure_birth_tree(limit,birth_rate=speciation, rng=None):
    "Generates a uniform-rate pure-birth process tree. "
    if rng is None:
        rng = GLOBAL_RNG 
    tree = dendropy.Tree()
    tree.seed_node.edge.length = 0.0
    leaf_nodes = tree.leaf_nodes()
    total_length = 0.0
    while total_length< limit: 
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
    waiting_time = rng.expovariate(len(leaf_nodes)/birth_rate)
    for nd in leaf_nodes:
        nd.edge.length += waiting_time
    tree.is_rooted = True
    return tree

"""
recursive model as described in Splitting_Tree.py
"""
def split(species_list,limit):    
    species = species_list[random.randint(0,len(species_list)-1)]
    increment = random.expovariate(speciation)
    if type(species.edge_length) == float:
        species.edge_length += increment
    else:
        species.edge_length = increment        
    species1 = species.new_child() 
    species2 = species.new_child()
    total_length = species.distance_from_root()
    species_list.remove(species)
    for elem in species_list:
        if type(elem.edge_length) == float:
            elem.edge_length += increment
        else:
            elem.edge_length = increment
    species_list += species.child_nodes()
    if total_length >= limit:
        return 'speciation complete'  
    else:
        split(species_list,limit)

"""
time_comparison for the two models
"""
def time_comparison():
    limit = 0
    while limit <= 1000:
        #time for recursive model
        rec_start = time.time()
        maintree = dendropy.Tree()
        species1 = maintree.seed_node.new_child()
        species2 = maintree.seed_node.new_child()
        species_list = maintree.seed_node.child_nodes()
        split(species_list,limit)
        rec_end = time.time()
             
        #time for iterative model
        iter_start = time.time()
        uniform_pure_birth_tree(limit)
        iter_end = time.time()

        print ("length limt: " + str(limit))
        print ("Is iteration faster?",(iter_end-iter_start)<(rec_end-rec_start))
        limit += 10


time_comparison()
