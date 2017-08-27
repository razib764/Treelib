import dendropy

char = dendropy.TaxonNamespace(['1','2','3'])

"""
Creating tree with 4 leaves
"""

tree1 = dendropy.Tree(taxon_namespace = char)

node1 = tree1.seed_node.new_child(label = 'A', edge_length = 1)
node2 = tree1.seed_node.new_child(label = 'B', edge_length = 1)

child11 = dendropy.Node(label = 'A', edge_length = 1)
child12 = dendropy.Node(label = 'B', edge_length = 2)
child21 = dendropy.Node(label = 'C', edge_length = 1)
child22 = dendropy.Node(label = 'D', edge_length = 2)

node1.set_child_nodes([child11,child12])
node2.set_child_nodes([child21,child22])


"""
The following method first sets the value of each node to 0.
If the evolution function is run over child 11 or child 22, the values of the nodes change
Finally, the values of the nodes are printed.
"""


def evolution(node):
    node1.value = 0
    if node == child11:
        tree1.preorder_edge_iter(child11)
        node1.value += 1
    node2.value = 0
    if node == child22:
        tree1.preorder_node_iter(child22)
        node2.value += 2
    print (node1.value)
    print (node2.value)

evolution(child11)
evolution(child12)
evolution(child21)
evolution(child22)



tree1.print_plot()
