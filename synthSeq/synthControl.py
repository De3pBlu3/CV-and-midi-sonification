import time
import CVbuffer

def sendStaticVoltage(channel,value):  # This function is called from synthSeq\CVbuffer.py
    """Sends a static voltage to be queued to the Arduino.

    Args:
        channel int: The channel you wish to send the voltage to.
        value float: Value between 0 and 5 volts to send to the Arduino.
    """
    
    if value > 5.0 or value < 0.0:
        print("Voltage out of range")
        return()
    if channel > 5 or channel < 0:
        print("Channel out of range")
        return()
    
    CVbuffer.queueVoltage(channel, value)

def sendRampUp(channel, start_voltage, end_voltage, duration):
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



