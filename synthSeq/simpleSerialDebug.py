import serial
from time import sleep
from CVbuffer import map_voltage


print("Attempting to open serial port")
ser = serial.Serial('COM3', 9600) # Open a serial connection to the Arduino on the specified port and baud rate
sleep(2)
print("Serial port opened on", 'COM3', "at", 9600, "baud")


channel = 2
voltage = 5


value = map_voltage(voltage)
ser.write(bytes('{:d} {:d}\n'.format(channel, value), 'utf-8'))