import math

print("a,b,c")

a = int(input())
b = int(input())
c = int(input())

if a==0:
    print("not a quandratic eqn ",-c/b)
else:
    d = b * b - 4 * a * c
    if d==0:
        root = -b/(2*a)
        print("real one root",root)
    elif d > 0:
        root1 = -b + math.sqrt(d)/(2*a)
        root2 = -b - math.sqrt(d)/(2*a)
        print("root 1 ",root1)
        print("root 2",root2)
    else:
        print("roots are imaginery")
        real_part = -b /(2*a)
        imaginary_part = math.sqrt(-d)/(2*a)
        print("Root 1 = {:.2f} + {:.2f}i".format(real_part, imaginary_part))
        print("Root 2 = {:.2f} - {:.2f}i".format(real_part, imaginary_part))