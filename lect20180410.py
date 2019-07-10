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
#to save it to file
#get the default path/directory
import os
os.getcwd()
#to change the path
os.chdir("C:\\Users\\saints.MARYVILLE\\Documents")
plt.savefig('threefunctions.png')
#second method to save a figure in Python
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
fig.savefig('three.eps')   # save the figure to file
plt.close(fig)   
#you plot the following two functions
#y1=sin(x)-x
#y2= 3*x+cos(x)
#save the figures into an eps file and load this file into Excel
x = np.arange(0,10, 0.01)
y1 = np.sin(x) -x
y2 = 3*x + np.cos(x)
fig = plt.figure() 

ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(x, y1, 'k', label='y =sin(x)-x')
ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(x, y2, 'g--', label='y =3x+cos(x)')
fig.savefig("myfig.eps")
# or
# plt.savefig("myfig.eps")
plt.close(fig)
#so far, we have plotted functions based on lower level library matplotlib
#we also could plot them using higher level packages
#pandas and searborn

import pandas as pd
#recall: Series is a one column of data
s = pd.Series(np.random.randn(10).cumsum(), 
             index=np.arange(0, 100, 10))
#seriesobj.plot
s.plot()
#we could multiple columns at the same time 
#using df.plot()
df = pd.DataFrame(np.random.randn(10, 4).cumsum(0),
 columns=['A', 'B', 'C', 'D'],
 index=np.arange(0, 100, 10))
df.plot()
#download returs.csv from lecture 8
#load the data into memory
#plot all the columns.
#first step specify the directory where the file is
import os
os.getcwd()
#change to current file
os.chdir("C:\\Users\\saints.MARYVILLE\\Downloads")
df = pd.read_csv("returns.csv") 
df.plot()
#bar plot
fig, axes = plt.subplots(2, 1)
#axes is a 2 row 1 column vector/
#mapping the regions
#axes[0]; axes[1]

data = pd.Series(np.random.rand(16), 
      index=list('abcdefghijklmnop'))
#data is a series
#series.plot.bar
#vertical bar
data.plot.bar(ax=axes[0], color='k', alpha=0.7)
#horizontal bar
data.plot.barh(ax=axes[1], color='k', alpha=0.7)
plt.show()

df = pd.DataFrame(np.random.rand(6, 4),
    index=['one', 'two', 'three', 'four', 'five', 'six'],
     columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
df.plot.bar()
#load the data
#download returs.csv from lecture 8
#load the data into memory
#bar plot all the rows
os.chdir("C:\\Users\\saints.MARYVILLE\\Downloads")
df = pd.read_csv("returns.csv") 
df.plot.bar()

#plot functions using searborn

# Import necessary libraries
import seaborn as sns #higher level plotting
import matplotlib.pyplot as plt #lower level plotting

# Load iris data
iris = sns.load_dataset("iris")
# Construct iris plot scatter plot swarmplot
sns.swarmplot(x="species", y="petal_length", data=iris)
# Show plot
plt.show()
