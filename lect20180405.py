# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
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
plt.show()
#step 5 save figure or functions into file
#see help info by tyying help(plt.savefig)
plt.savefig('threefunctions.pdf')
plt.savefig('figpath.png', dpi=400, bbox_inches='tight')

#import os
#os.getcwd()

#another long version to plot
#we could also generate fig and axes at the same time
#using plt.subplots(#rows, #columns)
#1 one figure, axes = 4 =2*2
#we index axes using syntax similar to numpy matrix
#we generate figure and axes at the same time
#then we could select aexs using syntax similar to numpy

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)
plt.subplots_adjust(wspace=0, hspace=0)
plt.savefig('figpath.svg')
#plt.savefig('figpath.png', dpi=400, bbox_inches='tight')

#############################
#customize the graphics

#short version
#specify line styles, colors, label etc
#help(plt.plot)
data = np.random.randn(30).cumsum()
plt.plot(data, 'k--', label='Default')
plt.plot(data, 'k-', drawstyle='steps-post', label='steps-post')
plt.legend(loc='best')
#plt two functions y= 2*x+1; y =sin(x)
#sepcify label: "y=2x+1"; "y=sin(x)"
#and plot legend
x = np.arange(100)
y1 = 2*x+1
y2 = np.sin(x)
plt.plot(x, y1, 'bo', label = "y=2x+1")
plt.plot(x, y2, 'rD', label = "y=sin(x)")
plt.legend(loc = 'best')
#long version to setup parameters such as
#line, color, legend etc
#step 1: load library
import matplotlib.pyplot as plt
import numpy as np
#step 2: prepare for the data
x = np.random.randn(1000).cumsum()
#step 3: generate a figure(paper/canvs)
fig = plt.figure()
#step 4 add subregion using axes
ax = fig.add_subplot(1, 1, 1)
#step 5 plot based on corresponding axes
ax.plot(x)
#step 6 customize our plot
#specify xticks
ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'],
    rotation=30, fontsize='small')
ax.set_title('My first matplotlib plot')
ax.set_xlabel('Stages')
ax.set_ylabel('cumsum')
#plot function utility cost
#c(t) = 1*t+50
#t= 70;71;...;100
t =np.arange(31)+70
c= 1*t+50
#step 3: generate a figure(paper/canvs)
fig = plt.figure()
#step 4 add subregion using axes
ax = fig.add_subplot(1, 1, 1)
#step 5 plot based on corresponding axes
ax.plot(t, c)
#specif the xticks [70, 80, 90, 100]
ticks = ax.set_xticks([70, 80, 90, 100])

#specify the xticks label ["nice", "mild", "hot", "very hot"]
labels = ax.set_xticklabels(["nice", "mild", "hot", "very hot"],
    rotation=30, fontsize='small')

#specify the title "Untility cost in Summer"
ax.set_title('Untility cost in Summer')

#specify the xlabel " temperature"
ax.set_xlabel('temperature')

#specify the ylabel "cost in dollars"
ax.set_ylabel('cost in dollar')

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
#draw two functions y1 =cos(x)^2; y2= sin(x)^2 
#on the same graph and add legend
x = np.arange(10)
y1 = np.cos(x)**2
y2 = np.sin(x)**2
#generate figure
fig = plt.figure() 
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y1, 'g', label='cos(x) Squared')
ax.plot(x, y2, 'k--', label='sin(x) Squared')
ax.legend(loc='best')