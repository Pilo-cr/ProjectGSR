import matplotlib.pyplot as plt 
import csv 

# TODO: This should be an argument
input = 'dataSamples/cleanLaughData.csv'

x = [] 
y = [] 

with open(input ,'r') as csvfile: 
	lines = csv.reader(csvfile, delimiter = ',') 
	
	for row in lines: 
		y.append(int(row[0])) 
		x.append(int(row[1])) 

plt.plot(x, y, color = 'g', linestyle = 'solid', label = "stress data") 
plt.xlabel('MilliSecs') 
plt.ylabel('Stress') 
plt.title('Laughing Stress', fontsize = 20)
plt.grid()
plt.legend() 
plt.show() 
