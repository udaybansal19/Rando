import matplotlib.pyplot as plt 
import array as arr
import random
import numpy as np
import random

numberOfPoints = 10000

x_coor = arr.array('d')
y_coor = arr.array('d')

x = 1
y = 2
c = 0
prime = [True for i in range(numberOfPoints + 1)]
nextPrime = arr.array('i')

def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    # all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    global prime
    global nextPrime 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers 
    for p in range(n + 1): 
        if prime[p]:
            nextPrime.append(p)             

def rand_func():
    SieveOfEratosthenes(numberOfPoints)
    global nextPrime
    global c
    c = c+1
    return nextPrime[c]

def next_point(z):

    global x
    global y

    x_coor.append(x)
    y_coor.append(y)

    if(z%6==1):
        x = (0 + x)/2
        y = (0 + y)/2
    elif(z%6==3):
        x = (2 + x)/2
        y = (3 + y)/2
    elif(z%6==5):
        x = (4 + x)/2
        y = (0 + y)/2


def chaos_game(x,y):

    for i in range(0,numberOfPoints):
        next_point(rand_func())



def plotIT():
	
	plt.plot(x_coor,y_coor,'.',color='blue') 
  
	plt.ylabel('Random number')  
	plt.xlabel('Seed')  
	plt.title('Random number with corresponding seed') 
  
	plt.show()

chaos_game(x,y)
plotIT()