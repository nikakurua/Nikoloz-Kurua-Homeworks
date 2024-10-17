
def isconsonant(a):
    vowels ="aeiouAEIOU "
    if a not in vowels and a.isalpha():
        return True

if "__main__" == __name__:
    input_word = input("Please enter a word and the program will return only consonants in this word: ")
    for i in input_word:
        if isconsonant(i):
            print(i, end = " ")
