import random

f = open("integer.txt",'w')

for i in range(500):
    number = random.randint(1,500)
    f.write(str(number) + '\n')
f.close()
            
