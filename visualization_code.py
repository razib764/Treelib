"""
The following code can be used to create .png files of the visualization of the
tree entered in the input
"""

import dendropy
from ete3 import Tree, TreeStyle

def draw(tree):
    string = tree.as_string(schema = "newick")
    string = string[4:]
    print(string)
    t = Tree(string)
    ts = TreeStyle()
    ts.show_branch_length = True
    ts.show_branch_support = True
    t.render("mytree.png")
    print('done')

tree = dendropy.model.birthdeath.birth_death_tree(1,0.0,max_time = 5)
draw(tree)
