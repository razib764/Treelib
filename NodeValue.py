import random
import dendropy

s1 = '((A:1,(B:2,(C:2,D:4),E:2,(F:2,G:4))));'
def process_node(node, start=1.0):
    if node.parent_node is None:
        node.value = start
    else:
        node.value = random.gauss(int(node.parent_node.value), int(node.edge.length))
    for child in node.child_nodes():
        process_node(child)
    if node.taxon is not None:
        print("%s : %s" % (node.taxon, node.value))

mle = dendropy.Tree.get(data = s1, schema='newick')
for node in mle.postorder_node_iter():
    if node.edge.length == None:
        node.edge.length = 1
process_node(mle.seed_node)


    
