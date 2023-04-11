import mido 
import threading
import multiprocessing
import time
import queue
import random
# list all midi ports
print(mido.get_output_names())

notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']

# send a midi message to the output port
outport = mido.open_output('PRO-1:PRO-1 MIDI 1 20:0')
debugMode = False
instruction_queue = queue.Queue()
KillThreadBool = False





# Define a function to accept user input and add it to the queue
def input_thread():
    # Get input from user
    #check if input is a float
    try:
        note = input("Enter note: ")
        octave = int(input("Enter octave: "))
        sendNote(octave, note)
    except ValueError:
        print("invalid input")

    
    # Add instruction to queue

#given an octave and a string, turn it into a midi note
def noteToMidi(octave, note):
    note = note.lower()
    #if note is a flat, we need to take the index before 
    if len(note) > 1:
        if note[1] == 'b':
            noteIndex = notes.index(note[0]) - 1
        else:
            noteIndex = notes.index(note) 
    else:
        noteIndex = notes.index(note)
    
    
    return noteIndex + (int(octave) + 1) * 12

def sendNote(octave,note,delay,channel):
    Midinote = noteToMidi(octave, note)
    instructionTemplate = (Midinote, delay, channel)
    instruction_queue.put(instructionTemplate)
    return "note sent"

def stopNote(delay, note,channel):
    time.sleep(delay)
    msg = mido.Message('note_off', note=note, channel=channel)
    outport.send(msg)

def clearNotes():
    outport.reset()

def queueCompleteThread():
    while KillThreadBool == False:
        # Get instruction from queue
        if instruction_queue.empty() == False:
            
            instruction = instruction_queue.get()
            Midinote = instruction[0]
            delay = instruction[1]  
            channel = instruction[2]
            # Process instruction
            #random velocity between 64-80
            velocity = random.randint(80,100)
            if debugMode == False:
                    print("sending note: ", Midinote, "for", delay, "seconds")
                    msg = mido.Message('note_on', note=Midinote, channel=channel, velocity=velocity)
                    outport.send(msg)
                    p = multiprocessing.Process(target=stopNote, args=(delay,Midinote,channel,))
                    p.start()
            else:
                None
                print("*Debug* Completed instruction, note: ", Midinote)
            # Mark instruction as complete
            instruction_queue.task_done()
            # print how many instructions are left in the queue
        else:
            None


# convert the melody to midi commands
def ConvertMelodyToMidi(octave, melody, channel, tempo):
    #itterate through the melody changing each note into a tuple with the note and the delay
    melody = [(note, 60/tempo) for note in melody]

    #if two notes are the same in order, remove the second one and add the delay to the first one
    try:
        for i in range(len(melody)-1):
            if melody[i][0] == melody[i+1][0]:
                melody[i] = (melody[i][0], melody[i][1] + melody[i+1][1])
                #delete the second note
                melody.pop(i+1)
    except:
        pass
    #send each note to the queue
    for note in melody:
        if note[0] == "rest":
            print("rest for ", note[1], "seconds")
            time.sleep(note[1])
        
        else: 
            sendNote(octave, note[0], note[1], channel)
            time.sleep(note[1])
        # print(note)




    # delay = 60/tempo
    # for note in melody:
    #     if note == "rest":
    #         print("rest for ", delay, "seconds")
    #         time.sleep(delay)
    #     else:
    #         sendNote(octave, note, delay, channel)
    #         print("Send note: ", note, "delay: ", delay)
    #         time.sleep(delay)


def endQueue():
    global KillThreadBool
    KillThreadBool = True
    instruction_queue.join()
    processing_thread.join()


#reset everything
clearNotes()

# Declare the input and processing threads
processing_thread = threading.Thread(target=queueCompleteThread)


print("starting Thread")
# Start the threads
processing_thread.start()
print("started Thread")


# generate a melody from a scale

# send a note

#close processing thread

#end the queue
# endQueue()
# processing_thread.join()

# #print all running threads
# # Wait for the threads to finish
# input_thread.join()
# processing_thread.join()

