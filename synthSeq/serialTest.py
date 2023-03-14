import serial
import math
from time import sleep
# Map a voltage value to a 12-bit value between 0 and 4095
def map_voltage(voltage):
    voltage = max(min(voltage, 5.0), 0.0)  # Limit voltage to range 0-5 volts
    value = int(math.floor((voltage / 5.0) * 4095.0))  # Map voltage to 12-bit value
    return value

#invert the map_voltage function
def map_value(value):
    value = max(min(value, 4095), 0)  # Limit value to range 0-4095
    voltage = int(math.floor((value / 4095.0) * 5.0))  # Map value to voltage
    return voltage

def read_analog_values(voltage, channel):
    #### Beginning serial communication
    print("Attempting to open serial port")
    ser = serial.Serial('COM3', 9600) # Open a serial connection to the Arduino on the specified port and baud rate
    sleep(2)
    print("Serial port opened on", 'COM3', "at", 9600, "baud")
    #### End of contact establishing
    ########################################
    value = map_voltage(voltage)
    ser.write(bytes('{:d} {:d}\n'.format(channel, value), 'utf-8')) # Send the "control" command to the Arduino
    
    sleep(2)
    values = []
    for i in range(4):
        line = ser.readline().decode('utf-8').rstrip() # Read a line of text from the serial connection and remove any trailing whitespace
        parts = line.split(':') # Split the line into two parts at the colon
        pin = int(parts[0].strip()[3:]) # Extract the pin number from the first part of the line
        value = int(parts[1].strip()) # Extract the analog value from the second part of the line
        values.append((pin, value)) # Add the pin and value to the list of values
    ser.close() # Close the serial connection
    return values


for i in read_analog_values(10,2):
    print("pin: ", i[0], "value: ", i[1], "voltage: ", map_value(i[1]), "V")