import threading
import CVbuffer
import synthControl
import time

CVbuffer.debugMode = False
CVbuffer.intialisation()

# Define a function to accept user input and add it to the queue
def input_thread():
    while True:
        # Get input from user
        #check if input is a float
        try:
            value = float(input("Enter value: "))
            channel = int(input("Enter channel: "))
        except ValueError:
            print("invalid input")
            continue
        
        synthControl.sendStaticVoltage(channel, value)
        # Add instruction to queue



# Declare the input and processing threads
input_thread = threading.Thread(target=input_thread)
processing_thread = threading.Thread(target=CVbuffer.queueCompleteThread)

# Start the threads
input_thread.start()
processing_thread.start()

# for i in range(5):
#     synthControl.sendRampUp(1, 0, 5, 5)
#     time.sleep(1.5)

#close processing thread

# CVbuffer.endQueue()

# processing_thread.join()

#print all running threads
# Wait for the threads to finish
# input_thread.join()
# processing_thread.join()

