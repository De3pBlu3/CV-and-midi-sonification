import serial
from time import sleep
import math
import queue
ser = None
instruction_queue = None

def intialisation(port="COM3", baudrate=9600):
    global instruction_queue
    global ser
    # ser = serial.Serial(port, baudrate)
    sleep(2)
    print("Serial port opened on", port, "at", baudrate, "baud")
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
    print(instructionTemplate, "instruction queued")
    instruction_queue.put(instructionTemplate)

#The function that continually goes over the instruction queue and sends the voltage to the arduino
def VoltageSendqueue():
    while True:
        # Get instruction from queue
        instruction = instruction_queue.get()
        # Process instruction
        print(instruction)
        # value = map_voltage(voltage)
        # ser.write(bytes('{:d} {:d}\n'.format(channel, value), 'utf-8'))

        # Mark instruction as complete
        instruction_queue.task_done()
            
                