# -*- coding: utf-8 -*-
"""
Created on Sun May 29 02:11:46 2022

@author: Admin
"""

import math as mt
 
MAXN = 1000000
 
# stores smallest prime factor for
# every number
spf = [0 for i in range(MAXN)]
 
# Calculating SPF (Smallest Prime Factor)
# for every number till MAXN.
# Time Complexity : O(nloglogn)
def sieve():
    spf[1] = 1
    for i in range(2, MAXN):
         
        # marking smallest prime factor
        # for every number to be itself.
        spf[i] = i
 
    # separately marking spf for
    # every even number as 2
    for i in range(4, MAXN, 2):
        spf[i] = 2
 
    for i in range(3, mt.ceil(mt.sqrt(MAXN))):
         
        # checking if i is prime
        if (spf[i] == i):
             
            # marking SPF for all numbers
            # divisible by i
            for j in range(i * i, MAXN, i):
                 
                # marking spf[j] if it is
                # not previously marked
                if (spf[j] == j):
                    spf[j] = i
 
# A O(log n) function returning prime
# factorization by dividing by smallest
# prime factor at every step
def getFactorization(x):
    ret = list()
    while (x != 1):
        ret.append(spf[x])
        x = x // spf[x]
 
    return ret
 
# Driver code
 
# precalculating Smallest Prime Factor
sieve()
x = 22150
print("prime factorization for", x, ": ",
                                end = "")
 
# calling getFactorization function
p = getFactorization(x)
 
for i in range(len(p)):
    print(p[i], end = " ")
 
# This code is contributed
# by Mohit kumar 29