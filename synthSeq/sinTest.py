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
timeoffSet=0.0001

values = []
# time the function
start = time.time()
for i in range(samples):
    value = midline + amplitude * math.sin(phase)  # Calculate the value of the sine wave at the current phase with adjusted midline and amplitude
    # print(value)  # Output the value (you can replace this with your own processing)
    # values.append(value)
    phase += phase_increment  # Increment the phase
    time.sleep((1 / sample_rate)-timeoffSet)  # Sleep to ensure that the total duration is one second

end = time.time()

# print(min(values))
# print(max(values))

print("Total time:", end - start)
print("Time selected:", duration)
print("Time difference:", end - start - duration)