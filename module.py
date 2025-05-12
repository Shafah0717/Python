def generate_square_dict():
    square_dict={}
    for i in range(1,7):
        square_dict[i]=i*i
    return square_dict
print(generate_square_dict())