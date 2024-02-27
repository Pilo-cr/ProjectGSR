import serial

try:
    arduino = serial.Serial("/dev/cu.usbmodem1101", timeout = 1)

    with open("data.txt", "w") as f:
        while True:
            unClean = arduino.readline()
            f.write(unClean.decode())
            f.flush()

except Exception as e:
    print("error: " , e)



