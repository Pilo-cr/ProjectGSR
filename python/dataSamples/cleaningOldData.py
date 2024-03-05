with open('dataSamples/data_laugh.txt','r') as oldFile, open("dataSamples/cleanLaughData.csv", 'w') as newFile: 
	oldlines = oldFile.readlines()
	
	for oldline in oldlines: 
		if len(oldline) >= 12:
			newline = oldline[2:]
			newline = newline[:-6]
			newline = newline.replace(";",",")
			newline = newline + '\n'
			newFile.write(newline)
			 