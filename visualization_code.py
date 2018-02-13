import dendropy

from ete3 import Tree, TreeStyle
string = dendropy.model.birthdeath.birth_death_tree(1,0.0,max_time=5).as_string(schema = "newick")
string = string[5:]
t = Tree(string)
ts = TreeStyle()
ts.show_leaf_name = True
t.render("mytree.png")
print('done')