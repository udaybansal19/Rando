import matplotlib.pyplot as plt 
import array as arr
import random 

x = arr.array('i')
y = arr.array('d')

for i in range(0,1000):
    random.seed(i) 
    y.insert(i,random.random())
    x.insert(i,i) 

plt.plot(x, y) 
  
plt.ylabel('Random number')  
plt.xlabel('Seed')  
plt.title('Random number with corresponding seed') 
  
plt.show() 