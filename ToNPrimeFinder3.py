# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:52:14 2015



This program finds prime numbers smaller than maxPrime.

Arttu Huttunen, Oulu, Finland. 2015.
"""

maxPrime = 1000000


#*****************
from bitarray import bitarray
import math

n = maxPrime +1
limit = math.sqrt(maxPrime)

a = bitarray(n)
a.setall(True)


k = 2   #number being investigated
i = 2   #multiple of k being marked as non prime
while k < limit:
    if a[k]:
        i = k + k
        while i < n:
            a[i] = False
            i = i + k
    k = k +1


a[0] = False
a[1] = False


primeSum = 0

for x,y in enumerate(a):
    if y == True:
#        print (x)   #prints the primes
#or calculate the sum of primes
        primeSum = primeSum + x
print (primeSum)