import serial
import math
import pdb
import array
import CRC
import random
import struct

PACKET_SIZE = 1024 #bits
BITS_IN_BYTE = 8
BYTES_PER_PACKET = PACKET_SIZE/BITS_IN_BYTE
HEADER = 0b01111110
CRC_DIV = 0b110101
FILE_SIZE = 9319 #bytes
PERCENT_ERRORS = 10

#read file
data = array.array('B')
f = open('umdlogo.jpg','rb')
data.fromfile(f,FILE_SIZE)


#how many packets do we need?
n_packets = int(math.ceil(len(data)/BYTES_PER_PACKET)+1)

#open serial port
ser = serial.Serial(0, 19200, timeout=5)

#main loop
for frame_counter in range(n_packets):
    msg = array.array('B')
    payload = array.array('B')
    msg.append(HEADER)
    msg.append(frame_counter)

    if frame_counter+1 == n_packets:
        #need a special case for last packet bc it's not full
        remaining_bytes = len(data) - frame_counter*BYTES_PER_PACKET
        for i in range(remaining_bytes):
            payload.append(data[i+frame_counter*BYTES_PER_PACKET])
            msg.append(data[i+frame_counter*BYTES_PER_PACKET])

    else:
        for byte in range(frame_counter*BYTES_PER_PACKET, (frame_counter+1)*BYTES_PER_PACKET):
            payload.append(data[byte])
            msg.append(data[byte])

    msg.append(CRC.ComputeCRC(payload, CRC_DIV))

    success = False

    while not(success):
        print 'Sending msg... ' , frame_counter

        x = random.randint(0,100)

        if x <= PERCENT_ERRORS:
            error = random.randint(0,len(msg))
            err_msg = array.array('B',msg.tostring())
            err_msg[error] = 0xFF
            ser.write(err_msg.tostring())
        else:
            ser.write(msg.tostring())

        if frame_counter < 10:
            ACK = ser.read(1)
        else:
            ACK = ser.read(2)
        if ACK != '':
            ACK = int(ACK)
            if ACK == frame_counter:
                print 'ACK for frame ', ACK, ' received.'
                success = True
        else:
            print 'ERROR!!! Resending'


#clean up
f.close()
ser.close()




