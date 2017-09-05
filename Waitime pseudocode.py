"""
The time of occurence of the nth event in a poisson process with rate lambda is:
    Tn = n/lambda (....verify?)

The tlength function calculates the total number of events (n) that can occur in a
poisson distrbution in total time 'limit'
n is the number of events: it starts at 0 and stops when the limit to the total
time is acheived

"""


def tlength():
    time = 0
    n = 0
    l = float(input("Enter lambda: "))
    limit = int(input("Enter time limit here: "))
 
    while time < limit:
        time += n/l
        n += 1
    print (n)

"""
We can set the limit to be the number of events instead of the time length
"""

"""
The above function can be implemented in dendropy by replacing the time with the
branch length and with each event, a new child can be added to the node.
"""
