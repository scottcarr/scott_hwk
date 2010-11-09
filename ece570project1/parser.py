import array

N_PACKETS = 72
MSG_SIZE = 131

f = open('test.txt','rb')
f_o = open('test.jpg','wb')

a = array.array('B')
slice = array.array('B')
try:
    a = a.fromfile(f, 100000)
except EOFError:
    print "Found end of file."

for i in range(N_PACKETS):
    slice = a[i*MSG_SIZE:(i+1)*MSG_SIZE]
    slice = slice[2:-1]
    print len(slice)
    slice.tofile(f_o)

slice = a[N_PACKETS*MSG_SIZE:]
slice = slice[2:-1]
slice.tofile(f_o)


f.close()
f_o.close()

