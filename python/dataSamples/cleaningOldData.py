with open('dataSamples/data_laugh.txt','r') as oldFile, open("dataSamples/cleanLaughData.csv", 'w') as newFile: 
	oldlines = oldFile.readlines()
	
	for oldline in oldlines: 
		if len(oldline) >= 12:
			newline = oldline[2:]
			newline = newline[:-6]

			data = newline.split(";")

			newline = data[0] + "," + str(int(data[1]) * 1000) + '\n'
			newFile.write(newline)
			 