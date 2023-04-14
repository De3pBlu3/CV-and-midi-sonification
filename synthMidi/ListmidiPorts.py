import mido 

#use this to get the midi input and output ports
for port in mido.get_input_names():
    print(port)
for port in mido.get_output_names():
    print(port)

