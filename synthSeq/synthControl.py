import time
import CVbuffer
import numpy as np
import matplotlib.pyplot as plt

def testIfSinisvalid(sineWaveVals):
    maxValue = round(sineWaveVals.max(),2)
    minValue = round(sineWaveVals.min(),2)
    if maxValue > 5:
        print("Unable to send raw signal:", str(maxValue)+"V", "is", str(maxValue-5)+"V", "too high")
        return(False)
    elif minValue < 0:    
        print("Unable to send raw signal:", str(minValue)+"V", "is", str(0-minValue)+"V", "too low")
        return(False)
    
    #If all tests have passed
    return(True)
        

def valueValidation(value,channel):
    if value > 5.0 or value < 0.0:
        print("Voltage out of range")
        return(False)
    if channel > 5 or channel < 0:
        print("Channel out of range")
        return(False)
    else:
        return(True)


def sendStaticVoltage(channel,value):  # This function is called from synthSeq\CVbuffer.py
    """Sends a static voltage to be queued to the Arduino.

    Args:
        channel int: The channel you wish to send the voltage to.
        value float: Value between 0 and 5 volts to send to the Arduino.
    """
    
    if valueValidation(value,channel):
        CVbuffer.queueVoltage(channel, value)

def sendRampUp(channel, start_voltage, end_voltage, duration):
    """Send a ramp up to be queued to the Arduino.

    Args:
        channel (int): The channel you wish to send the voltage to.
        start_voltage (float): The voltage to start the ramp at.
        end_voltage (float): The voltage to end the ramp at.
        duration (float): The duration of the ramp in seconds.
    """

    if valueValidation != True:
        return()
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
    """Send a ramp down to be queued to the Arduino.

    Args:
        channel (int): The channel you wish to send the voltage to.
        start_voltage (float): The voltage to start the ramp at.
        end_voltage (float): The voltage to end the ramp at.
        duration (float): The duration of the ramp in seconds.
    """
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

def envelopeRampUp(channel, start_voltage, end_voltage, duration):
    """Send a ramp up to be queued to the Arduino.

    Args:
        channel (int): The channel you wish to send the voltage to.
        start_voltage (float): The voltage to start the ramp at.
        end_voltage (float): The voltage to end the ramp at.
        duration (float): The duration of the ramp in seconds.
    """
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

def sinWave(channel, freq):
    """Send a sin wave to be queued to the Arduino.

    Args:
        channel (int): The channel you wish to send the voltage to.
        freq (float): The frequency of the sin wave.
    """
    resolution = 10000000 # how many datapoints to generate

    length = np.pi * 2 * freq
    signal = np.sin(np.arange(0, length, length / resolution))*2.5
    signal = (signal+2.5)

    if testIfSinisvalid(signal) == True:
        #Send sin wave to CVbuffer
        for i in range(len(signal)):
            CVbuffer.queueVoltage(channel, signal[i])
            time.sleep(1/len(signal))