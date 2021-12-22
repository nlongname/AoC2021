with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
    f.close

packets = {}
#format is startBit:[version, type, endBit(or None),value(or None)]
#if ID=1 (it's not a literal) value is the number of subpackets
#(in which case endBit starts as None, but will update later) 
#if it's a literal, value is the value

#data =['C0015000016115A2E0802F182340']
data = bin(int(data[0],16))[2:]
front_pad = 0
if len(data)%4 != 0:
    front_pad = 4 - (len(data)%4)
data = '0'*front_pad + data

def analyze_packet(bitstream:str,startBit:int = 0) -> None:
    if bitstream.count('1') == 0:
        return
    pointer = 0
    packetVersion = int(bitstream[pointer:pointer+3],2)
    pointer += 3
    packetType = int(bitstream[pointer:pointer+3],2)
    pointer += 3
    if packetType != 4:
        packetID = bitstream[pointer]
        pointer += 1
        if packetID == '0':
            subpacketLen = int(bitstream[pointer:pointer+15],2)
            pointer += 15
            packetLen = pointer+subpacketLen
            packets[startBit] = [packetVersion, packetType, startBit+packetLen,None]
            analyze_packet(bitstream[pointer:packetLen],startBit+pointer)
            analyze_packet(bitstream[packetLen:],startBit+packetLen)
        else:
            subpackets = int(bitstream[pointer:pointer+11],2)
            pointer += 11
            packets[startBit] = [packetVersion, packetType, None, subpackets]
            analyze_packet(bitstream[pointer:],startBit+pointer)
    else:
        value = ''
        while bitstream[pointer] == '1':
            value += bitstream[pointer+1:pointer+5]
            pointer += 5
        value += bitstream[pointer+1:pointer+5]
        value = int(value,2)
        pointer += 5
        #pointer = pointer-(pointer%4)+4
        packets[startBit] = [packetVersion, packetType, startBit+pointer, value]
        analyze_packet(bitstream[pointer:],startBit+pointer)

analyze_packet(data)

print(sum([packets[x][0] for x in packets]))
