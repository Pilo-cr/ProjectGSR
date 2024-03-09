# Used to make still graph of old data files, you can upload any.

import matplotlib.pyplot as plt 
import csv 

# TODO: This should be an argument
input = 'dataSamples/listening_vs_working.csv'

x = [] 
y = []

with open(input ,'r') as csvfile: 
	lines = csv.reader(csvfile, delimiter = ',') 
	
	for row in lines: 
		y.append(int(row[0])) 
		x.append(int(row[1])) 

plt.plot(x, y, color = 'g', linestyle = 'solid', label = "stress data") 
plt.xlabel('millliseconds')
plt.ylabel('Stress') 
plt.title('Stress Levels', fontsize = 20)
plt.grid()
plt.legend() 
plt.show() 
