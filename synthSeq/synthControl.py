from timeing import sleep_precisely
import time
import CVbuffer
import math

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
        print("Sent static voltage", value, "to channel", channel)
    else:
        print("Failed to send static voltage")

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

def sinWave(channel, frequency=1):
    """Send a sin wave to be queued to the Arduino.

    Args:
        channel (int): The channel you wish to send the voltage to.
        freq (float): The frequency of the sin wave.
    """


    sample_rate     =     100  # Sample rate (in Hz)
    duration        =     1  # Total duration of the sine wave (in seconds)
    samples         =     int(sample_rate * duration)  # Total number of samples
    phase_increment =     2 * math.pi * frequency / sample_rate  # Phase increment for each sample
    phase           =     0  # Starting phase
    midline         =     2.5  # Midline of the sine wave
    amplitude       =     2.5  # Amplitude of the sine wave
    print(1/sample_rate)
    # time the function
    start = time.time()
    for i in range(samples):
        CVbuffer.queueVoltage(channel, midline + amplitude * math.sin(phase))
        phase += phase_increment  # Increment the phase
        time.sleep((0.0033))  # Sleep to ensure that the total duration is one second
    end = time.time()

    print("Total time:", end - start)
    print("Time selected:", duration)
    print("Time difference:", end - start - duration)

def tempSinWave():
    frequency = 1  # Frequency of the sine wave (in Hz)
    sample_rate = 75  # Sample rate (in Hz)
    duration = 1  # Total duration of the sine wave (in seconds)
    samples = int(sample_rate * duration)  # Total number of samples
    phase_increment = 2 * math.pi * frequency / sample_rate  # Phase increment for each sample
    phase = 0  # Starting phase
    midline = 2.5  # Midline of the sine wave
    amplitude = 2.5  # Amplitude of the sine wave

    start = time.time()
    for i in range(samples):
        value = midline + amplitude * math.sin(phase)  # Calculate the value of the sine wave at the current phase with adjusted midline and amplitude
        phase += phase_increment  # Increment the phase
        time.sleep(1 / sample_rate)  # Sleep to ensure that the total duration is one second
    end = time.time()

    print("Total time:", end - start)
    print("Time selected:", duration)
    print("Time difference:", end - start - duration)