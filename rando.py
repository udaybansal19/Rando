import matplotlib.pyplot as plt 
import array as arr
import random

itr = 1000

randNum = arr.array('d')
growthRate = arr.array('d')

def func(x,r):
  return r*x*(1-x)

def rando(ini,r):

	x = ini
	for i in range(0,itr):
		x = func(x,r)

	for i in range(0,1000):
		x = func(x,r)
		randNum.append(x)
		growthRate.append(r)

def plotRando(x):
	
	for i in range(0,600):
		rando(x,i/100)
	
	plt.plot(growthRate,randNum,'.') 
  
	plt.ylabel('Random number')  
	plt.xlabel('Seed')  
	plt.title('Random number with corresponding seed') 
  
	plt.show() 	

itr = 1000
x = 0.2
r = 3
# print("Using logistics equation")
# print("Initial Values: r: ",r,"  x: ",x)
# print("Number of iterations: ",itr)
plotRando(x)
