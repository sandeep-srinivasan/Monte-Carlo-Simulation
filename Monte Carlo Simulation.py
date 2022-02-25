#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing the modules
from scipy import random
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# limits of integration
a = 0
b = 2
N = 100

# function to calculate the integral of a particular value of x
def f(x):
    return np.exp(-x**2)

# list to store all the values for plotting
values = []

#Iterating through the number of samples
for i in range(N):

    #array of zeros of length N
    ar = np.zeros(N)

    # iterating over each Value of ar and filling it with a randome value between the limits a and b
    for i in range (len(ar)):
        ar[i] = random.uniform(a,b)

    # variable to store sum of the functions of different values of x
    integral = 0.0

    # iterates and sums up values of different functions of x
    for i in ar:
        integral += f(i)
        
    ans = (b-a)/float(N)*integral
    
    values.append(ans)

# plot of the distribution
plt.title("Distributions of areas calculated")
plt.hist (values, bins=30, ec="black")

plt.xlabel("Areas")
plt.show()


# In[3]:


# Calculating the Confidence interval for the answer of the integral
x_bar = np.mean(values)
stdev = np.std(values)
sample_size = N
confidence_coefficient = 1.96 #95% confidence

margin_of_error = confidence_coefficient*(stdev/np.sqrt(sample_size))

lower_bound = x_bar - margin_of_error

upper_bound = x_bar + margin_of_error

print ("The average value calculated by monte carlo integration is {}.".format(x_bar))

print ("The upper bound value calculated by monte carlo integration is {}.".format(upper_bound))

print ("The lower bound value calculated by monte carlo integration is {}.".format(lower_bound))

