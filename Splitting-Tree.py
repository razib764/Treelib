import random
import dendropy

maintree = dendropy.Tree()

'''
We will split maintree according to a poisson distribution.
The root of the tree first splits into two nodes
The two initial child nodes will be involved in further splitting
'''
species1 = maintree.seed_node.new_child()
species2 = maintree.seed_node.new_child()
species_list = maintree.seed_node.child_nodes()

limit = float(input("Enter limit on the length: ")) #this will determine the stopping point of the splitting

'''
split is a recursive funtion that:
    1. Choses a random flat between 0 and 1 as a rate of speciation (lambda)
    2. Coses a random child node (species) to speciate
    3. Generated a random exponential variable (depending on the rate of speciation) as the incremnet in time
    4. Speciates the chosen node into two child nodes
    5. Increments the remaining nodes so that the total length of all the nodes remains equal
    6. Repeats the process recursively until maximum total length is acheived
'''

def split(species_list):

    speciation = 1.0 #random.random()
    print ("Speciation will occur at a rate of: " + str(speciation))
    
    species = species_list[random.randint(0,len(species_list)-1)]
    print ("Speciation will occur to: "+ str(species))

    increment = random.expovariate(speciation)
    #If the species has just formed from a spltting, edge length is 'None'(not a float),
    #so the '+=' operator doesn't work
    if type(species.edge_length) == float:
        species.edge_length += increment
    else:
        species.edge_length = increment
    print("Branch langth has increased by: " + str(increment))
        
    #speciation
    species1 = species.new_child() 
    species2 = species.new_child()
    print ("Speciation has occured")

    total_length = species.distance_from_root()
    print("New length of the branches will be: " + str(total_length))

    """
    In the following step, the list of species is updated.
    The species that split is removed and the child nodes of that species are added instead
    """
    #generating the new species list,
    species_list.remove(species)
    
    #updating the other elements in the list for length
    for elem in species_list:
        if type(elem.edge_length) == float:
            elem.edge_length += increment
        else:
            elem.edge_length = increment
    print("Remaining species have caught up in time")
    #adding the new childnodes to the list of species
    species_list += species.child_nodes()
    
    #Recursion step
    if total_length >= limit: #base case
        return 'speciation complete'  
    else:
        split(species_list)

split(species_list)
maintree.print_plot()
print(maintree.as_string(schema="newick"))
