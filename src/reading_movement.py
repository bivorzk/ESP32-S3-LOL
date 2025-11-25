import serial, time

ser = serial.Serial('COM3', 9600)  # Not correct update when device ready
time.sleep(2)  # 


ser.write(b'Hello, world!\n')

with open('src/resource/mouse_movements.txt', 'r') as file:
    for line in file:
        ser.write(line.encode())
        time.sleep(0.34)

ser.close()
