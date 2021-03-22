with open('strange.dat') as ss:
    a = ss.readlines()
    f = open('strange.png', 'w+b')
    byte_arr = [int(octet[:-1], 2) for octet in a]
    binary_format = bytearray(byte_arr)
    f.write(binary_format)
    f.close()
