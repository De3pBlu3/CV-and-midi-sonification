import math
import time

frequency = 1  # Frequency of the sine wave (in Hz)
sample_rate = 300  # Sample rate (in Hz)
duration = 1  # Total duration of the sine wave (in seconds)
samples = int(sample_rate * duration)  # Total number of samples
phase_increment = 2 * math.pi * frequency / sample_rate  # Phase increment for each sample
phase = 0  # Starting phase
midline = 2.5  # Midline of the sine wave
amplitude = 2.5  # Amplitude of the sine wave

for i in range(samples):
    value = midline + amplitude * math.sin(phase)  # Calculate the value of the sine wave at the current phase with adjusted midline and amplitude
    print(value)  # Output the value (you can replace this with your own processing)
    phase += phase_increment  # Increment the phase
    time.sleep(1 / sample_rate)  # Sleep to ensure that the total duration is one second


print(min(samples))
print(max(samples))