import dendropy

BigTree = dendropy.Tree()

count = 0

while count < 10:
    node = BigTree.seed_node.new_child()
    node.label = str(count)
    node.edge_length = 1
    count1 = 0
    while count1 < 10:
        child = dendropy.Node()
        child.label = str(count)+str(count1)
        child.edgelength = 1
        node.add_child(child)
        count1 += 1        
    count += 1
BigTree.print_plot()
        
