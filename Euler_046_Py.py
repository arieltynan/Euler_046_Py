#Ariel Tynan
# Euler Problem 046 Goldbach's other conjecture, Solved in Python
# Started and solved 4March2022

import math


def odd_Nums(l): # generate array of odd numbers 2*l + 1
    odds = []
    for i in range(0,l):
        odds.append(2*i + 1)
    return odds

def prime_Sieve(n): #Function modified from Geeksforgeeks
     
    primes = [] # initial empty list of primes
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers
    for p in range(n + 1):
        if prime[p] and p % 2 != 0:
            primes.append(p)
    return primes
 
oList = odd_Nums(1000000) # Creates list of odd numbers. oList[0] = 1
pList = prime_Sieve(500000) # Creates list of primes for use

for i in pList: #primes
    num = int((i - 1)/2)
    oList[num] = 0 #removes primes, leaves composites
    for j in range(1,40): #squares
        num = int((i + 2*j*j - 1)/2)
        oList[num] = 0

for k in range(0,len(oList) - 1):
    if oList[k] != 0 and k > 1:
        print(k*2 + 1)
        break

#Prints answer








