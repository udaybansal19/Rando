import matplotlib.pyplot as plt 
import array as arr
import random
import numpy as np

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

def plotFunc(r):
	x = np.linspace(-3,3,100)
	y = func(x,r)

	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.spines['left'].set_position('center')
	ax.spines['bottom'].set_position('zero')
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')

	plt.plot(x, y,'r')
	plt.plot(x,func(func(x,r),r))
	plt.plot(x,func(func(func(x,r),r),r))
	plt.show() 	

def plotRando(x):
	
	eff = 100
	for i in range(0*eff,10*eff):
		rando(x,i/eff)
	
	plt.plot(growthRate,randNum,'.',color='black') 
  
	plt.ylabel('Ouput Value from function after many iterations')  
	plt.xlabel('Growth Rate (r)')  
	plt.title('Logistic Map') 
  
	plt.show() 	

itr = 1000
x = 0.1
r = 1
plotRando(x)
#plotFunc(r)