import matplotlib.pyplot as plt 
import array as arr
import random

itr = 1000

randNum = arr.array('i')
growthRate = arr.array('d')

def func(x,r):
  return r*x*(1-x)

def rando(ini,r):

	x = ini
	for i in range(0,itr):
		x = func(x,r)

	for i in range(0,10):
		x = func(x,r)
		print(x)
		#randNum.append(i,x)

itr = 1000;
x = 0.2;
r = 3;
print("Using logistics equation")
print("Initial Values: r: ",r,"  x: ",x)
print("Number of iterations: ",itr)
rando(x,r);