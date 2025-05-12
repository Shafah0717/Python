def separate_number():
    inFile = open("num.txt",'r')
    pos_File = open("pos.txt",'w')
    neg_File = open("neg.txt",'w')

    for line in inFile:
        line = line.strip()
        if line:
            num = int(line)
            if num>=0:
                pos_File.write(f"{num} \n")
            else:
                neg_File.write(f"{num} \n")
    print("separation completed")
separate_number()