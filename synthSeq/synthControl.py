import time
import math
import CVbuffer

def UsersendVoltage(channel,value):  # This function is called from synthSeq\CVbuffer.py
    while True:
        CVbuffer.queueVoltage(channel, value)

def sendRampUp(channel, start_voltage, end_voltage, duration):
    # Calculate the voltage increment for each iteration
    num_steps = 100  # Number of voltage steps
    voltage_increment = (end_voltage - start_voltage) / num_steps

    for i in range(num_steps):
        # Calculate the current voltage value for this iteration
        voltage = start_voltage + i * voltage_increment
        # Map the voltage to a 12-bit value and send it to the Arduino
        print(voltage)
        CVbuffer.queueVoltage(channel, voltage)
        # Wait for a short period of time before sending the next voltage value
        time.sleep(duration / num_steps)

def sendRampDown(channel, start_voltage, end_voltage, duration):
    # Calculate the voltage increment for each iteration
    num_steps = 100  # Number of voltage steps
    voltage_increment = (start_voltage - end_voltage) / num_steps

    for i in range(num_steps):
        # Calculate the current voltage value for this iteration
        voltage = start_voltage - i * voltage_increment
        # Map the voltage to a 12-bit value and send it to the Arduino
        print(voltage)
        CVbuffer.queueVoltage(channel, voltage)
        # Wait for a short period of time before sending the next voltage value
        time.sleep(duration / num_steps)



# def sendVoltage(channel, voltage):
#     # Map the voltage to a 12-bit value and send it to the Arduino
#     value = map_voltage(voltage)
#     ser.write(bytes('{:d} {:d}\n'.format(channel, value), 'utf-8'))

