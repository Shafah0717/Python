bitString = input("enter the binary string")
exponent = len(bitString) -1
decimel=0

for bit in bitString:
    decimel += int(bit) * (2 ** exponent)
    exponent = exponent - 1
print(decimel)