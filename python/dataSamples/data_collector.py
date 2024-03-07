import serial

# TODO: This should be a program argument
serial_port = "/dev/cu.usbmodem1101"
data_file_location = "data.txt"

try:
    # Connect to the serial port where Arduino is streaming data
    arduino = serial.Serial(serial_port, timeout = 1)

    with open(data_file_location, "w") as f:
        while True: # This loop will run until press Ctrl+C
            streamed_line = arduino.readline()
            f.write(streamed_line.decode())
            f.flush()

except Exception as e:
    print("error: " , e)



