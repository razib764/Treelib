import random
import dendropy

s1 = '((A:1,(B:2,(C:2,D:4):1,E:2,(F:2,G:4):1):2):3);'

##The following function assigns random continous values to the nodes of the tree.
def process_node(node, start=1.0):
    if node.parent_node is None:
        node.value = start
    else:
##      The random.gauss funtion takes the mean to be the value of the parent node and the
##      standard deviation to be the length of the edge of the node. This way, the 
##      values of the nodes are dependent on those variables.
        node.value = random.gauss(int(node.parent_node.value), int(node.edge.length))
    for child in node.child_nodes():
        process_node(child)
    if node.is_leaf() == True:
    ##Fially, this adds the value to the label of the leaf
       node.taxon.label += ': ' + str(node.value)




##The following method assigns discrete attributes to the nodes of the tree. There are two possible attributes, 0 and 1.
##The probability of an attribute being 0 is 68% and the same being 1 is 32%. Similar to the process_node() function,
##this function assigns attributes to the nodes using the gaussian distribution, where the mean is the attribute of
##the parent node and the standard deviation is the length of the edge of the node. 
def process_node_discrete(node, start=0):
    if node.parent_node is None:
        node.attribute = start
    else:
##        The random.gauss function takes the mean to be the value of the parent node and the standard deviation
##        to be the edge length of the node. In a standard gaussian distribution, 68% of the data lies between a
##        standard deviation of the mean.
        node.attribute = random.gauss(int(node.parent_node.attribute), int(node.edge.length))
        lower = node.parent_node.attribute - node.edge.length
        upper = node.parent_node.attribute + node.edge.length
##        There is 68% probablity that the attribute lies inside the lower and the upper value range. Therfore, the
##        probablity of node.attribute being 1 is 32% and the same being 0 is 68%
        if node.attribute >= upper or node.attribute <= lower:
            node.attribute = 1
        else:
            node.attribute = 0
    for child in node.child_nodes():
        process_node_discrete(child)
    if node.is_leaf() == True:
       node.taxon.label += ': ' + str(node.attribute)
       

mle = dendropy.Tree.get(data = s1, schema='newick')
process_node(mle.seed_node)
mle.print_plot()

mle_1 = dendropy.Tree.get(data = s1, schema='newick')
process_node_discrete(mle_1.seed_node)
mle_1.print_plot()




    
