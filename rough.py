import random 

def shuffle(word):
    new_word = random.sample(word,k=len(word))
    return "".join(new_word)

def new_func(word,score):
    res = shuffle(word)
    print("Arrange the letters to form valid word")
    print(res)
    user_inp = input()
    uppercase_word = user_inp.upper()
    if word == uppercase_word:
        print("Correct")
        print()
        score += 1
    else:
        print("Wrong")
        print()
        score -= 1
    return score 


def main():
    score = 0
    words = ["COUNTRY","WORD","HAPPY","CAR","DOG"]
    words = random.sample(words,k=len(words))
    for word in words:
        score = new_func(word,score)

    return score 
print("your final score is",main())