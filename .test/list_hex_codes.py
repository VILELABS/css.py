def Hex(r,g,b): # HEX color
    return '#%02x%02x%02x' % (r,g,b)

hexcodes = open('hexcodes.txt', 'a+')
for r in range(0,256,16):
    for g in range(0,256,16):
        for b in range(0,256,16):
            print(Hex(r,g,b))
            hexcodes.write(Hex(r,g,b) + "\n")