import math
import array

BITS_IN_BYTE = 8

def ComputeCRC(msg,divisor):

    sr = 0;

    bits = math.floor(math.log(divisor,2))

    # first divide the actual msg (later do the added zeroes)
    for byte in msg:
        for bit in range(1,BITS_IN_BYTE+1):
            sr = sr <<  1
            if (byte >> (BITS_IN_BYTE-bit)) & 1:
                sr = sr + 1
            #print sr
            if sr >= (2**bits):
                sr = sr ^ divisor

    # do the added zeros
    for i in range(0,int(bits)):
        sr = sr <<  1
        if sr >= (2**bits):
            sr = sr ^ divisor

    return sr
