action = input("Enter action (e/d) :")
while action != "e" and action != "d":
    action = input(" The action can be only \"e\" or \"d\". \"e\" for cipher and \"d\" for decipher: ")

qwerty = "qwertyuiopqasdfghjklazxcvbnmz"

if action == "e":
    input_word = input("Please enter a word and you will get the ciphered word :")
    ciphered_word = ""
    for i in input_word:
        if i in qwerty:
            ciphered_word += qwerty[qwerty.index(i)+1]
        else: ciphered_word += i

    print (ciphered_word)

else:
    input_word = input("Please enter a word and you will get the deciphered word :")
    deciphered_word = ""
    for i in input_word:
        if i in qwerty:
            deciphered_word += qwerty[qwerty.rindex(i) - 1]
        else:
            deciphered_word += i

    print(deciphered_word)

