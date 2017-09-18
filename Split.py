import dendropy
new_tree = dendropy.Tree()
edge = new_tree.seed_node.new_child()
#length_limit = int(input("Enter length limit here: "))

def split(edge):
    """
    This is an attempt at a recursive function that splits edges.
    The function is incomplete because it does not work for more than two cycles
    """
    edge.edge.length = 3 #length of the first edge
    #the following two lines adds two children to the node at the edge
    #this is the splitting
    edge1 = edge.new_child() 
    edge2 = edge.new_child()

    total_length = edge.distance_from_root() #would be the limiting factor
    
    while total_length < 6: #length of 6 is only 2 iterations
        split(edge1)
        split(edge2)
        total_length = edge1.distance_from_root()
        print (total_length)

    new_tree.print_plot()    
    
    
