import dendropy
from dendropy.utility import GLOBAL_RNG
import matplotlib.pyplot as plt

#generate a tree
tree = dendropy.model.birthdeath.birth_death_tree(1.0,0.2,max_time = 5.0)
# Returns distance of node furthest from root
total_time = tree.max_distance_from_root()
# Divide time span into 10 steps
step = float(total_time) / 10
# To store tuples of (time, number of lineages)
ltt = []
# Start at first time step
current_time = step
while current_time < total_time:
    # Get number of lineages at current time
    num_lineages = tree.num_lineages_at(current_time)
    # Store it
    ltt.append( (current_time, num_lineages) )
    # Move to next time step
    current_time += step
if current_time < total_time:
    ltt.append( (total_time, tree.num_lineages_at(total_time)) )
# Print results
time = [0]
num_lin = [0]    
for t, num_lineages in ltt:
    if num_lineages >= max(num_lin): #make sure that the nodes do not decrease
        time += [t]
        num_lin += [num_lineages]
    print("{:12.8f}\t{}".format(t, num_lineages))
time.remove(0)
num_lin.remove(0)
#m_num = max(num_lin)
plt.axis([0.0,5, 0,max(num_lin)+10])
plt.plot(time,num_lin)
plt.show()
    
