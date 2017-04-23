"""
The following code assigns discete attributes to the nodes of a tree. 

"""


import random
import dendropy

"""

process_node method assigns discrete attributes to the nodes of the tree. There are two possible attributes, 0 and 1.
The root starts with a atrribute of 0 and the possibility of a child acquiring a different attribute than its parent is 10%.

"""

def process_node(node, start=0):
    if node.parent_node is None:
        node.attribute = start
    
    else:
        #random floats between 0 and 1 are generated
        prob_number = random.random()
        """
        The probability of the random float (prob_number) being greater than 0.9 is 10%
        So, the probability of the node.attribute changing is 10%
        """
        if prob_number >= 0.9:
            if node.parent_node.attribute == 0:
                node.attribute = 1
            else:
                node.attribute = 0
        else:
            node.attribute = node.parent_node.attribute
    for child in node.child_nodes():
        process_node(child)
    if node.is_leaf() == True:
       node.taxon.label += ': ' + str(node.attribute)


mle = dendropy.Tree.get(
    path='pythonidae.mle.nex.txt',
    schema='nexus')
process_node(mle.seed_node)

mle.print_plot()
