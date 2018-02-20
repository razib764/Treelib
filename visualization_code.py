import dendropy

from ete3 import Tree, TreeStyle
string = dendropy.model.birthdeath.birth_death_tree(1,0.0,max_time=5).as_string(schema = "newick")
string = string[5:]
#check if the plotting is wrong or the tree
t = Tree(string)
ts = TreeStyle()
ts.show_leaf_name = True
ts.show_branch_length = True
ts.show_branch_support = True
t.render("mytree.png")
print('done')