import serial
ser = serial.Serial("COM3", 9600)

#send two intergers to the arduino
print("1 4095".encode())
ser.write("1 4095".encode())
