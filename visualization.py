# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 11:28:16 2018

@author: yliu3
"""
#to save a figure using plt.savefig() or fig1.savefig() is indeed the way to save an image.

#step 1 load the package
import matplotlib.pyplot as plt
import numpy as np
#step 2: prepare for the data: manually from df, SQL
x= np.arange(100)
y1 =np.tan(x)
y2 = x**3+1
y3 = np.exp(x)
#step 3: create a plot using figure /Canvas/paper
fig = plt.figure()
# step 4: plot using axes: partication of the figure
#add_subplot(#of rows, #of columns, the current index)
#since we have two functions to plot
#we could have 3 rows, 1 column, or 1 row 2 columns
ax1 = fig.add_subplot(3, 1, 1)
ax1.plot(x,y1)
ax2 = fig.add_subplot(3, 1, 2)
ax2.plot(x,y2)
ax3 = fig.add_subplot(3, 1, 3)
ax3.plot(x,y3)
#if it doesn't show the graph, call plt.show() explcityly
#step 5 save figure or functions into file
#see help info by tyying help(plt.savefig)
plt.savefig('threefunctions.pdf')



import matplotlib.pyplot as plt
from numpy.random import randn
fig = plt.figure() 
#we have one region to plot
#we plot 3 functions on the same region/axes
ax = fig.add_subplot(1, 1, 1)
ax.plot(randn(1000).cumsum(), 'k', label='one')
ax.plot(randn(1000).cumsum(), 'k--', label='two')
ax.plot(randn(1000).cumsum(), 'k.', label='three')
ax.legend(loc='best')
fig.savefig('three.png')   # save the figure to file
plt.close(fig)   