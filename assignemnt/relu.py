# Assignment1
#1. ReLU

#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#ReLU
def ReLU(x): return np.maximum(0,x)

#input value
x=np.linspace(-10,10,100) #generate 100 values bw -10 to 10
y=ReLU(x)

#plot
plt.plot(x,y)   #line graph x axis we have input values and y axis is the relu fn
plt.title("ReLU curve")
plt.xlabel('x')
plt.ylabel('y')
plt.show()
