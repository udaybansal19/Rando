import matplotlib.pyplot as plt 
import array as arr
import random
import numpy as np
import random

numberOfPoints = 100

# Prime numbers didn't work
# TODO: Rando  refactoring and check
# TODO: Digits of pi and other irrational numbers

x_coor = arr.array('d')
y_coor = arr.array('d')

x = 1
y = 2
c = 0

randNum = arr.array('d')
growthRate = arr.array('d')

def func(x,r):
  return r*x*(1-x)

def rando(ini,r):

	x = ini
	for i in range(0,100):
		x = func(x,r)

	for i in range(0,100):
		x = func(x,r)
		randNum.append(x)
		growthRate.append(r)

def rand_func():
    eff = 10
    global c
    for i in range(0*eff,4*eff):
        rando(x,i/eff)
    c = c+1
    return randNum[c]*1000

def next_point(z):

    global x
    global y

    x_coor.append(x)
    y_coor.append(y)

    if(z%3==0):
        x = (0 + x)/2
        y = (0 + y)/2
    elif(z%3==1):
        x = (2 + x)/2
        y = (3 + y)/2
    elif(z%3==2):
        x = (4 + x)/2
        y = (0 + y)/2


def chaos_game(x,y):

    for i in range(0,numberOfPoints):
        next_point((int)(rand_func()))



def plotIT():
	
	plt.plot(x_coor,y_coor,'.',color='blue') 
  
	plt.ylabel('Random number')  
	plt.xlabel('Seed')  
	plt.title('Random number with corresponding seed') 
  
	plt.show()

chaos_game(x,y)
plotIT()