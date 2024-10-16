input_word = input("Please enter a string: ")

for i in range(0,len(input_word),2):
    if input_word[i] == "e":
        continue
    print (input_word[i], end = " ")

