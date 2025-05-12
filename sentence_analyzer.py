def analyze_sentence(sentence):
    words= sentence.split()

    sumOfword = len(words)
    digit = sum(c.isdigit() for c in sentence)
    uppercase = sum(c.isupper() for c in sentence)
    lowercase = sum(c.islower() for c in sentence)

    print("no of words",sumOfword)
    print("toatl no of digit",digit)
    print("total no of uppercase",uppercase)
    print("total no of lowercase",lowercase)

sentence = input("enter the sentence")
analyze_sentence(sentence)
