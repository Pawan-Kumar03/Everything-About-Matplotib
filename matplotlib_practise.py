# -*- coding: utf-8 -*-
"""Matplotlib-Practise.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1inu8M_sWgm1PA4YyKQYIdN7PoVNiMTD5

#**Everything about Matplotlib**
"""

import matplotlib.pyplot as plt
import numpy as np

xAxis = np.array([0,5])
yAxis = np.array([0,25])

plt.plot(xAxis, yAxis)
plt.title("staight line")
plt.show()

plt.plot(yAxis) #xAxis will be taken by default from 0 to len(yAxis)
plt.show()

plt.plot(xAxis, yAxis,'o') #from start point till end point
plt.title('start-end points')
plt.show()

xAxis = np.array([1, 20, 13, 34, 5, 67, 75, 80, 93, 100])
yAxis = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

plt.plot(xAxis, yAxis, marker='o')
plt.title('marker')
plt.show()

plt.plot(xAxis, yAxis,'o:r') # o for marker, : for dotted line & r for red
plt.title('formate String --> marker|Line|Color')
plt.show()

plt.plot(xAxis, yAxis, marker='*', ms=20)
plt.title('Marker Size')
plt.show()

plt.plot(xAxis, yAxis, marker='*', ms=20, mec='r')
plt.title('Marker Color')
plt.show()

plt.plot(xAxis, yAxis, marker='*', ms=20, mfc='r')
plt.title('Marker Face Color')
plt.show()

plt.plot(xAxis, yAxis, linestyle = 'dotted')
plt.title('Linestyle')
plt.show()

plt.plot(xAxis, yAxis, marker='*', ms=20, mfc='r', linewidth = '5')
plt.title('Line Width')
plt.show()

line1 = np.array([3,8,5,10])
line2 = np.array([6,3,8,12])

plt.plot(line1, color='r', marker='o', mec='b')
plt.plot(line2, color='b', marker='o', mec='r')
plt.title('Multiple Lines')
plt.show()

plt.plot(xAxis, yAxis, marker='o', mfc='r')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Plot with Labels')
plt.show()

plt.plot(xAxis, yAxis, marker='o', mfc='r')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Plot with Grid')
plt.grid()
plt.show()

plt.plot(xAxis, yAxis, marker='o', mfc='r')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Plot with Grid')
plt.grid(color='green')
plt.show()

line1 = np.array([3,8,5,10])
line2 = np.array([6,3,8,12])
#subplot 1
plt.subplot(1, 2, 1) #the figure has 1 row, 2 columns, and this plot is the first plot.
plt.plot(line1, marker='o', mfc='r')
plt.title('Plot 1') # title for subplot
#subplot 2
plt.subplot(1, 2, 2) #the figure has 1 row, 2 columns, and this plot is the second plot.
plt.plot(line2, marker='o', mfc='r')
plt.title('Plot 2') # title for subplot

plt.suptitle('Two plots in One') # title of entire Fig
plt.show()

plt.scatter(xAxis, yAxis)
plt.title('Scatter Plot')
plt.show()

x = ['A', 'B', 'C', 'D', 'E']
y = [10, 20, 30, 40, 50]

plt.bar(x, y, width=0.1, color='r')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Bar Graph')
plt.show()

x = ['A', 'B', 'C', 'D', 'E']
y = [10, 20, 30, 40, 50]

plt.barh(x, y, height=0.1, color='b')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Bar Graph(Horizontal)')
plt.show()

#NumPy to randomly generate an array with 250 values, where the values will concentrate around 170, and the standard deviation is 10
x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.title('Histogram')
plt.show()

pie = np.array([35, 25, 25, 15])
mylabels = ['CS', 'BBA', 'Bed','EE']
# Legend: To add a list of explanation for each wedge
plt.pie(pie, labels=mylabels, startangle=90)
plt.title('Pie Chart')
plt.legend(title='Departments')
plt.show()