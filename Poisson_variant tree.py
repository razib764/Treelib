from math import exp
import dendropy
import random

"""
The ptree function creates a tree that splits into two with the probability of
a poisson distribution.
Of the branches that split, only one carries on the further splittng processes

For a poisson distribution, the probability that no arrivals occur in a given time interval is give by:
        P = e^(-lambda*time interval)
        
Arrivals in our case are events when the node splits.
The time interval here is the length of the edges of the tree.
"""

def ptree(l,limit,limit_type):

    poisson_tree = dendropy.Tree()
    
    """
    starting with length 0
    split is a variable that increments if the node splits
    limit is when the maximum total length or the maximum number of nodes is acheived and the function stops
    the function gives the user the ability to chose between the types of limits
    """

    length = 0
    split = 0

    if limit_type == 'l':
        
        while length <= limit:
            """
            Generating a probability of arrival.
            We are incrementing the length by 1, so the formula reduces to:
                    P = exp(-lambda)
                    'l' represents lambda
            """
            prob = exp(-l)
            rando = random.random()

            """
            The seed node has different functions for adding chidlren,
            so, the first split is separated from the other
            """
            if split == 0:
                """
                If the randomly created number is les that the probability of no splitting (prob),
                the node will split and so, two new children are added
                and the 'split' variable is incremented
                The new nodes are node1 and node2, but only node1 splits further
                """
                if rando < prob:
                    node1 = poisson_tree.seed_node.new_child()
                    node2 = poisson_tree.seed_node.new_child()
                    split += 1
            else:
                """
                Similarly, for the nodes other than the seed, the splitting occurs as
                child1 and child2 ad child1 becomes the new node1 for the next iteration
                """
                if rando < prob: 
                    child1 = dendropy.Node()
                    child2 = dendropy.Node()
                    node1.add_child(child1)
                    node1.add_child(child2)
                    split += 1
                    node1 = child1

            length += 1
 #       poisson_tree.print_plot()
        return split
    
    elif limit_type == 'n':

        """
        We repeat the same process, except we set the number of nodes
        (quatified by the value of 'split') as an upper limit
        """
            
        while split <= limit:
            prob = exp(-l)
            rando = random.random()
            if split == 0:
                if rando < prob:
                    node1 = poisson_tree.seed_node.new_child()
                    node2 = poisson_tree.seed_node.new_child()
                    split += 1
            else:
                if rando < prob: 
                    child1 = dendropy.Node()
                    child2 = dendropy.Node()
                    node1.add_child(child1)
                    node1.add_child(child2)
                    split += 1
                    node1 = child1

            length += 1
#        poisson_tree.print_plot()
        return length

"Generating graphs of the functions"

import matplotlib.pyplot as plt
import numpy
import matplotlib.mlab
import random

listl1= [] #list of number of nodes with limits on length and lambda 1
listl2= [] #list of number of nodes with limits on length and lambda 2
listl3= [] #list of number of nodes with limits on length and lambda 3
listn1 = [] #list of total length of edges with limits on number of nodes and lambda 1
listn2 = [] #list of total length of edges with limits on number of nodes and lambda 2
listn3 = [] #list of total length of edges with limits on number of nodes and lambda 3

count = 0
while count <= 10000:
    listl1 += [ptree(1,100,'l')]
    listl2 += [ptree(2,100,'l')]
    listl3 += [ptree(3,100,'l')]
    listn1 += [ptree(1,100,'n')]
    listn2 += [ptree(2,100,'n')]
    listn3 += [ptree(3,100,'n')]
    count += 1
#plotting histograms
plt.hist(listl1)
plt.hist(listl2)
plt.hist(listl3)
plt.hist(listn1)
plt.hist(listn2)
plt.hist(listn3)

    
