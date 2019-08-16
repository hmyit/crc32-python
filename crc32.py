#Created by Huseyin Meric Yigit
table = []
for byte in range(256):
    crc = 0
    for bit in range(8):
        if (byte ^ crc) & 1:
            crc = (crc >> 1) ^ 0xEDB88320
        else:
            crc >>= 1
        byte >>= 1
    table.append(crc)

def crc32(string):
    value = 0xffffffff

    for ch in string:
        value = table[(ord(ch) ^ value) & 0x000000ff] ^ (value >> 8)

    return hex(value)
