
import dendropy

new_tree = dendropy.Tree()
edge = new_tree.seed_node.new_child()
limit = 30

"""
The following sunction will recursively split the edges of the tree into two edges.
Each edge is of length 3.
The recursion stops when the total length of the tree reaches a certain limit.
Base case of the recursion is when the tree reaches the length limit in the first split.
"""

def split(edge):
    
    edge.edge.length = 3 #length of the first edge
    
    #the following two lines adds two children to the node at the edge
    #this is the splitting
    edge1 = edge.new_child() 
    edge2 = edge.new_child()
    
    total_length = edge.distance_from_root() #would be the limiting factor

    if total_length >= limit: #base case
        return 'done'  
        
    else: #recursion with the child nodes of the parent edges
        split(edge1)
        split(edge2)
        return 'done'


split(edge)
new_tree.print_plot()

    
  
    
    
