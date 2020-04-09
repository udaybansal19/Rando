import matplotlib.pyplot as plt 
import array as arr
import random
import numpy as np
import random

numberOfPoints = 100000

# Prime numbers didn't work
# Rando works!!!
#   Gives somewhat shape for r=3 as well
#
#   Value above bifurcation r=3.6 to r=4 gives perfect fractal
#   with disintegration below it
# Digits of pi and other irrational numbers
#   Digits of pi work!!
#   Digits of all irrational numbers work
#   Iterate different functinos with different growth rate

x_coor = arr.array('d')
y_coor = arr.array('d')

x = 1
y = 2
c = 0


def rand_func():
    eff = 100
    global c
    for i in range(3.6*eff,4*eff):
        rando(x,i/eff)
    c = c+1
    return randNum[c]*1000

def next_point(z):

    global x
    global y

    x_coor.append(x)
    y_coor.append(y)
    
    int(z)

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

    f = open("irrational_numbers/root2.txt", "r")
    for i in range(1,numberOfPoints):
        a = f.read(1)
        if((a != ' ') and (a != '')):
            next_point(int(a))



def plotIT():
	
	plt.plot(x_coor,y_coor,'.',color='blue') 
  
	# plt.ylabel('Random number')  
	# plt.xlabel('Seed')  
	plt.title('') 
  
	plt.show()

chaos_game(x,y)
plotIT()