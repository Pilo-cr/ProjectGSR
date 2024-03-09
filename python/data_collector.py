# Makes moving graph using current data being collected from arduino. 

import serial
import matplotlib.pyplot as plt
from statistics import mean 
from pydub import AudioSegment
from pydub.playback import play


# TODO: This should be a program argument
serial_port = "/dev/cu.usbmodem1101"
data_file_location = "dataSamples/data.csv"

message = ""

try:
    # Connect to the serial port where Arduino is streaming data
    arduino = serial.Serial(serial_port, timeout = 1)

    x = []
    y_mean = []
    y_last_30sec = []
    y = []
    song = AudioSegment.from_file("warning.mp3", format="mp3")
    
    plt.ion()
    plt.title('Realtime Stress', fontsize = 20)
    plt.show()

    with open(data_file_location, "w") as f:
        while True: # This loop will run until press Ctrl+C
            streamed_line = arduino.readline().decode()
            if len(streamed_line) > 0:
                f.write(streamed_line)
                f.flush()

                data_splitted = streamed_line.strip().split(",")
                y.append(int(data_splitted[0]))
                x.append(int(data_splitted[1]))
                y_mean.append(mean(y))
                y_last_30sec.append(mean(y[-10:]))

                # TODO: Make only part of line change colour instead of entire line?
                if int(data_splitted[0]) >= 500:
                     colour_change = 'r' # TODO:would like to make sound play when stres increases X amount intead of at a certain point.
                     play(song)
                else:colour_change = 'g'

                message = "Running time: " + data_splitted[1] + " Your average stress level has been: " + str(mean(y))
                print(message, end='\r')
                plt.plot(x, y, color = colour_change, linestyle = 'solid', label = "stress data")
                # This following line would desplay the active mean of your stress on the graph aswell, I chose to keep it off.
                # plt.plot(x, y_mean, color = 'b', linestyle = 'solid', label = "stress data")
                plt.plot(x, y_last_30sec, color = 'black', linestyle = 'solid', label = "stress data")
                plt.draw()
                plt.pause(0.1)

                # TODO: When key pressed, stop code from running. Stop gracely. 

# This prints the exact error thats occuring so we can see where exactly the code is going wrong.
except Exception as e:
    print("error: " , e)

print(message)
