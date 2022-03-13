#Weekly task 8
#Program called plottask.py that displays a plot of the functions 
#f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
#Author: Jarlath Scarry

import numpy as np
import matplotlib.pyplot as plt

#range(0,4) changed to np.linespace to plot 20 points for hightr resolution plot
#https://stackoverflow.com/questions/477486/how-to-use-a-decimal-range-step-value
xValues = np.linspace(0,4,20) 

#defining the functions the functions f(x)=x, g(x)=x2 and h(x)=x3

#setting the values the functions f(x)=x, g(x)=x2 and h(x)=x3
fValues = xValues  
gValues = [x*x for x in xValues]
hValues = [x*3 for x in xValues]

#setting the figure size #https://stackabuse.com/change-figure-size-in-matplotlib/
plt.rcParams["figure.figsize"] = [7, 4]
plt.rcParams["figure.autolayout"] = True

#plotting the functions and adding labels 
plt.plot(xValues, fValues, label= "f(x)=x",color="blue",)
plt.plot(xValues, gValues, label= "g(x)=x^2",color="red",)
plt.plot(xValues, hValues, label= "h(x)=x3",color="green",)

#set font dictionary for fonts https://www.w3schools.com/python/matplotlib_labels.asp
font1 = {'family':'serif','color':'blue','size':12}
font2 = {'family':'serif','color':'darkred','size':12}
font3 = {'family':'serif','color':'black','size':10}

#displaying the axis labels
plt.xlabel('X axis',fontdict=font3)
plt.ylabel('Y axis',fontdict=font3)


#displaying the chart title (and calling the fonts)
plt.suptitle('Weekly Task 8', fontdict=font1, y=.96) #suptitle moved vertically with y=.94
plt.title('Plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4]',fontdict=font2)
plt.legend()

plt.savefig('plottaskPlot.png')
plt.show()