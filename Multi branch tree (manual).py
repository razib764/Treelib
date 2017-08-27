import dendropy

"""
The following code creates two trees: tree_1 and tree_2 that have 9 nodes each.
The leaf nodes are labelled alphabetically
The print_plot() command prints the map of the trees
"""

taxon_namespace = dendropy.TaxonNamespace(["A","B","C","D","E","F"])

tree_1 = dendropy.Tree(taxon_namespace = taxon_namespace)
child_1 = tree_1.seed_node.new_child(edge_length = 1)
child_2 = tree_1.seed_node.new_child(edge_length = 1)
child_3 = tree_1.seed_node.new_child(edge_length = 1)
child_4 = dendropy.Node(edge_length=1)
child_5 = dendropy.Node(edge_length=2)
child_6 = dendropy.Node(edge_length=1)
child_7 = dendropy.Node(edge_length=2)
child_8 = dendropy.Node(edge_length=1)
child_9 = dendropy.Node(edge_length=2)
child_1.set_child_nodes([child_4, child_5])
child_2.set_child_nodes([child_6, child_7])
child_3.set_child_nodes([child_8, child_9])

child_4.taxon = taxon_namespace.get_taxon("A")
child_5.taxon = taxon_namespace.get_taxon("B")
child_6.taxon = taxon_namespace.get_taxon("C")
child_7.taxon = taxon_namespace.get_taxon("D")
child_8.taxon = taxon_namespace.get_taxon("E")
child_9.taxon = taxon_namespace.get_taxon("F")

print(tree_1.as_string("newick"))
tree_1.print_plot()

tree_2 = dendropy.Tree(taxon_namespace = taxon_namespace)
child_1 = tree_2.seed_node.new_child(edge_length = 1)
child_2 = tree_2.seed_node.new_child(edge_length = 1)
child_3 = tree_2.seed_node.new_child(edge_length = 1)
child_4 = dendropy.Node(edge_length=1)
child_5 = dendropy.Node(edge_length=2)
child_6 = dendropy.Node(edge_length=1)
child_7 = dendropy.Node(edge_length=2)
child_8 = dendropy.Node(edge_length=1)
child_9 = dendropy.Node(edge_length=2)
child_1.set_child_nodes([child_5, child_4])
child_2.set_child_nodes([child_6, child_7])
child_3.set_child_nodes([child_8, child_9])

child_4.taxon = taxon_namespace.get_taxon("A")
child_5.taxon = taxon_namespace.get_taxon("B")
child_6.taxon = taxon_namespace.get_taxon("C")
child_7.taxon = taxon_namespace.get_taxon("D")
child_8.taxon = taxon_namespace.get_taxon("E")
child_9.taxon = taxon_namespace.get_taxon("F")

print(tree_2.as_string("newick"))
tree_2.print_plot()

"""
The following code which tries to test the equality of the trees does not work
"""s
print(tree_1.preorder_node_iter() == tree_2.preorder_node_iter())
