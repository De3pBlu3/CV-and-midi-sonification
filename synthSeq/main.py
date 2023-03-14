import threading
import CVbuffer
import synthControl

CVbuffer.debugMode = True
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

# Wait for all instructions to be processed before exiting
CVbuffer.instruction_queue.join()
