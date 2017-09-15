from math import exp
import dendropy
import random

"""
The cust_arrival function crates a simulation for customer arrival where
Time measures the total time between customer arrivals
NumberCust measures the number of customers

The arrival process is a poisson process. Lambda is stored as l
The time between two arrivals is a random exponential variable dependent on l.

The customer arrival simulation adds new customers with a while loop.
TThere are two types of limitations on the loop:
1. Number of customers
2. Total time of the arrival process
'n' is for number of customers and 't' is for tottal time

The tree inputs are:
 'l' : value of lambda
 'limit_type': 'n' or 't'
 'limit': The number of customers or the total time where the loop stops

"""

def cust_arrival(l,limit_type,limit):
    
    """
    starting with Time and NumberCust of 0
    """

    Time = 0
    NumberCust = 0

    """
    limit_type of 't' returns the total number of customers who visited the shop in that time limit
    """

    if limit_type == 't':
        
        while Time < limit:
            NumberCust += 1
            Time += random.expovariate(l) #poisson arrival
        return (NumberCust)

    """
    limit_type of 'n' returns the total time taken by the limit nunmber of customers
    """
    
    if limit_type == 'n':
            
        while NumberCust < limit:
            NumberCust += 1
            Time += random.expovariate(l) #poisson arrival
        return (Time)

"Generating graphs of means Total time and number of customers over different lambdas"

import matplotlib.pyplot as plt
import numpy
import matplotlib.mlab
import random

arrive_hist = [] #list of means of number of arrivals in a limited time
time_hist =[]#list of means of total times with a limited number of arrivals
lambda_hist = []

lambdacount = 0.1
while lambdacount <= 10:
    
    arrive_list = [] #list of arrivals in limited time
    time_list = [] #list of total times with limited arrivals
    lambda_hist += [lambdacount]
    
    count = 0
    while count < 100:
        arrive_list += [cust_arrival(lambdacount,'t',1000)]
        time_list += [cust_arrival(lambdacount,'n',1000)]
        count += 1
    
    sumOfArrivals = 0
    for elem in arrive_list:
        sumOfArrivals += elem
    MeanA = sumOfArrivals/count
    arrive_hist += [MeanA]

    sumOfTimes = 0
    for elem in time_list:
        sumOfTimes += elem
    MeanT = sumOfTimes/count
    time_hist += [MeanT]
    
    lambdacount += 0.1

plt.plot(lambda_hist, arrive_hist)
plt.plot(lambda_hist, time_hist)
