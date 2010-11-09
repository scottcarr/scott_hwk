import serial
import pdb
import array
import CRC
import struct

N_PACKETS = 73
MSG_SIZE = 131
LAST_PACKET_SIZE = 106
ACK = 1
CRC_DIV = 0b110101
HEADER = 0b01111110

ser = serial.Serial(7,19200,timeout=11)
f_o = open('test.jpg','wb')

buffer = array.array('B')
output = array.array('B')

for i in range(N_PACKETS):
    print 'Reading packet ...', i
    success = False

    if i != 72:
        my_msg_size = MSG_SIZE
    else:
        my_msg_size = LAST_PACKET_SIZE

    while not(success):
        raw = ser.read(my_msg_size)
        buffer.fromstring(raw[2:-1])
        crc_expected = struct.unpack('B',raw[-1])
        crc_computed = CRC.ComputeCRC(buffer,CRC_DIV)
        header_recieved = struct.unpack('B',raw[0])

        if (CRC.ComputeCRC(buffer,CRC_DIV) == crc_expected[0]) and (header_recieved[0] == HEADER):
            print "Good CRC & header"
            output.fromstring(raw[2:-1])
            success = True
            ser.write(int(i))
        else:
            print "Bad CRC or header... waiting for resend."
        buffer = array.array('B')
        raw=[]

output.tofile(f_o)
ser.write(ACK)

f_o.close()


    
    
