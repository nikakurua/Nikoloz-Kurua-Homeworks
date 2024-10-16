input_word = input("Please enter a word :")
i = 0
while i < 5 :
    print( F"The first letter in the given word is: {input_word[0]} ")
    print(F"The Last letter in the given word is: {input_word[-1]} ")
    if len(input_word) % 2 == 0:
        middle_index_1 = int(len(input_word)/2 - 0.5)
        middle_index_2 = int(len(input_word) / 2 + 0.5)
        print(F"The number of letters in the given word is even, so you can see middle two letters in the given word: {input_word[middle_index_1]},{input_word[middle_index_2]}",end = 3 * "\n")

    else: print (f"The middle letter in the given word is {input_word[int(len(input_word)/2)]}", end = 3 * "\n")
    i += 1



