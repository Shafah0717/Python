decimel_number = int(input("enter the decimel "))

if decimel_number == 0:
    binary_number = 0
else:
    binary_number = ""
    while decimel_number>0:
        remainder = decimel_number % 2
        binary_number = str(remainder) + binary_number
        decimel_number = decimel_number // 2
print("binary value is =", binary_number)