import serial


def clean(L): #L is a list
    newL = [] #initializing new list
    for i in range(len(L)):
        temp=L[i][2:]
        newL.append(temp[:-5])
    return newL

def write(list):
    file = open("data.txt", mode='w')
    for i in range(len(list)):
        file.write(list[i]+'\n')
    file.close()



try:
    arduino = serial.Serial("/dev/cu.usbmodem1101", timeout = 1)

    with open("data.txt", "w") as f:
        while True:
            f.write( str(arduino.readline()).strip() + "\n" )
            f.flush()



    """initialising variables"""
    rawdata = []
    count = 0

    """receiving data and storing it in a list"""
    while count<3:
        rawdata.append(str(arduino.readline()))
        count += 1
    
    print(rawdata)

    cleanData = clean(rawdata)

    write(cleanData)

except Exception as e:
    print("error: " , e)



