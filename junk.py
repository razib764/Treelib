from copy import deepcopy

"""
-------------------------------------------------------------------------------
There are two ways that cdr could be valid for a given sequence 'alpha' and
a given element 'elem':
    1. (elem+1) is in alpha
    2. (elem-1) is in alpha
cdrValid1 and cdrValid2 test these two properties. The return True if 'elem'
can be used as a pointer for a cdr move.
-------------------------------------------------------------------------------
"""
def cdrValid1(alpha,elem):
    if -(elem+1) in alpha:
        return True
    return False
def cdrValid2(alpha,elem):
    if -(elem-1) in alpha:
        return True
    return False
"""
-------------------------------------------------------------------------------
cdrPointers prints out a list of all tuples that are possible pointers for cdr
for 'alpha'. It uses cdrValid1 and cdrValid2 tp determine all the valid points.
-------------------------------------------------------------------------------
"""

def cdrPointers(alpha):
    valid = [] #initiate list of valid pointers
    for elem in alpha:
        #We have to make sure that if for example (2,-3) is in the list, (-3,2)
        #is not also in the list.
        if cdrValid1(alpha,elem)and [-(elem+1),elem] not in valid:
            valid += [[elem,-(elem+1)]]
        if cdrValid2(alpha,elem) and [-(elem-1),elem] not in valid:
            valid += [[elem,-(elem-1)]]
    return valid
"""
-------------------------------------------------------------------------------
The following function performs a cdr over a permutation alpha ('list obj')
over the elements a1 and a2. The elements are entered in the order in which
the output is desired. a1 will appear as is and a2 will appear as it's additive
inverse behind a1.
-------------------------------------------------------------------------------
cdr first determines which element is at a lower index. Then it basically
flips the subarray between [a1+1,...,a2] and multiplies each element in the
subarray by -1
-------------------------------------------------------------------------------
"""

def cdr(alpha,a1,a2):
    i1 = alpha.index(a1) #Manages the indices
    i2 = alpha.index(a2)
    if i2 > i1:
        #this is the case where the first element appears earlier in the list
        i1 += 1 #rotate each element after a1
        while i2 >= i1: #rotation step
            k1 = alpha[i1]
            k2 = alpha[i2]
            alpha[i1] = -k2
            alpha[i2] = -k1
            i1 += 1
            i2 -= 1
        return (alpha)
    elif i1 > i2:
        #this is the case where the first element appears later in the list
        i1 -= 1 #rotate every element after a2
        while i1 >= i2: #rotation step
            k1 = alpha[i1]
            k2 = alpha[i2]
            alpha[i1] = -k2
            alpha[i2] = -k1
            i2 += 1
            i1 -= 1
        return (alpha)
"""
-------------------------------------------------------------------------------
autoCDR uses all of the above functions to do cdr on a given permutation alpha
-------------------------------------------------------------------------------
"""
def autoCDR(alpha):
    #print("Doing cdr for: " + str(alpha))
    results = []
    pointers = cdrPointers(alpha)
    for pair in pointers:
        beta = deepcopy(alpha)
        if pair[0] < 0:
            if -1*pair[0] > pair[1]:
                if alpha.index(pair[0]) < alpha.index(pair[1]):
                    results += [cdr(alpha,pair[0],pair[1])]
                    #print('Pointer: '+ str(pair)+' Result: '+ str(alpha))
                    alpha = beta
                elif alpha.index(pair[0]) > alpha.index(pair[1]):
                    results += [cdr(alpha,pair[1],pair[0])]
                    #print('Pointer: '+ str(pair)+' Result: '+ str(alpha))
                    alpha = beta
            if -1*pair[0] < pair[1]:
                if alpha.index(pair[0]) > alpha.index(pair[1]):
                    results += [cdr(alpha,pair[0],pair[1])]
                    #print('Pointer: '+ str(pair)+' Result: '+ str(alpha))
                    alpha = beta
                elif alpha.index(pair[0]) < alpha.index(pair[1]):
                    results += [cdr(alpha,pair[1],pair[0])]
                    #print('Pointer: '+ str(pair)+' Result: '+ str(alpha))
                    alpha = beta
        if pair[0] > 0:
            if pair[0] > -1*pair[1]:
                if alpha.index(pair[0]) < alpha.index(pair[1]):
                    results += [cdr(alpha,pair[1],pair[0])]
                    #print('Pointer: '+ str(pair)+' Result: '+ str(alpha))
                    alpha = beta
                elif alpha.index(pair[0]) > alpha.index(pair[1]):
                    results += [cdr(alpha,pair[1],pair[0])]
                    #print('Pointer: '+ str(pair)+' Result: '+ str(alpha))
                    alpha = beta
            elif pair[0] < -1*pair[1]:
                if alpha.index(pair[0]) < alpha.index(pair[1]):
                    results += [cdr(alpha,pair[0],pair[1])]
                    #print('Pointer: '+ str(pair)+' Result: '+ str(alpha))
                    alpha = beta
                elif alpha.index(pair[0]) > alpha.index(pair[1]):
                    results += [cdr(alpha,pair[0],pair[1])]
                    #print('Pointer: '+ str(pair)+' Result: '+ str(alpha))
                    alpha = beta
    return results

#testing below
#alpha = [1,3,-2]
#print(autoCDR(alpha))

from itertools import permutations,product

def SignedPermutations(items):
    for p in permutations(items):
        for signs in product([-1,1], repeat=len(items)):
            yield [a*sign for a,sign in zip(p,signs)]

longList = list(SignedPermutations([1,2,3]))

for elem in longList:
    print(elem)
    print(autoCDR(elem))
    print ("done")