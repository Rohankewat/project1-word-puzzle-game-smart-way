import random
def shuffle(word):
    new_word = random.sample(word,k=len(word))
    return "".join(new_word)

def new_func(word,score):
    another_call = shuffle(word)
    print("Arrange the letters to form a valid word")
    print(another_call)
    input_word = input()
    change_word = input_word.upper()
    if word == change_word:
        print("Correct")
        print()
        score = score+1
    else:
        print("Wrong")
        print()
        score = score-1
    return score
def main():
    score = 0 
    words = ["BREAK","FATHER","COUNTRY","EASY","NICE"]
    words = random.sample(words,k=len(words))
    for word in words:
        score = new_func(word,score)
        

    return score
print("your finall score is",main())