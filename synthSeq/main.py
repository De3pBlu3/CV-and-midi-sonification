import threading
import CVbuffer

CVbuffer.intialisation()

# Define a function to accept user input and add it to the queue
def input_thread():
    while True:
        # Get input from user
        value = float(input("Enter value: "))
        channel = int(input("Enter channel: "))
        # Add instruction to queue
        CVbuffer.queueVoltage(channel, value)



# Start the input and processing threads
input_thread = threading.Thread(target=input_thread)
processing_thread = threading.Thread(target=CVbuffer.VoltageSendqueue)

input_thread.start()
processing_thread.start()

# Wait for all instructions to be processed before exiting
CVbuffer.instruction_queue.join()
