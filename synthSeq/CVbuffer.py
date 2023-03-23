import serial
from time import sleep
import math
import queue
debugMode = False
ser = None
instruction_queue = None

def intialisation(port="COM3", baudrate=9600):
    global instruction_queue
    global ser
    if debugMode == False:
        ser = serial.Serial(port, baudrate)
        sleep(2)
        print("Serial port opened on", port, "at", baudrate, "baud")
    else:
        print("Debug mode activated, no serial port opened")
    instruction_queue = queue.Queue()

def closeSerial():
    global ser
    # Close serial port
    ser.close()
    print("Serial port closed")

# Map a voltage value to a 12-bit value between 0 and 4095
def map_voltage(voltage):
    voltage = max(min(voltage, 5.0), 0.0)  # Limit voltage to range 0-5 volts
    value = int(math.floor((voltage / 5.0) * 4095.0))  # Map voltage to 12-bit value
    return value


#Queue a voltage and a channel to be added to the instruction queue
def queueVoltage(channel, voltage):
    value = map_voltage(voltage)
    instructionTemplate = (channel, value)
    # print(instructionTemplate, "instruction queued")
    instruction_queue.put(instructionTemplate)

#The function that continually goes over the instruction queue and sends the voltage to the arduino
def queueCompleteThread():
    while True:
        # Get instruction from queue
        instruction = instruction_queue.get()
        voltage = instruction[1]
        channel = instruction[0]
        # Process instruction
        if debugMode == False:
            value = map_voltage(voltage)
            ser.write(bytes('{:d} {:d}\n'.format(channel, value), 'utf-8'))
            print("Completed instruction, channel:", channel, "voltage:", voltage)
        else:
            print("*Debug* Completed instruction, channel:", channel, "voltage:", voltage)
            pass
        # Mark instruction as complete
        instruction_queue.task_done()
            
                