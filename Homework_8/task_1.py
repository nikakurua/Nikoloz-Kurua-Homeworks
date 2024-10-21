input_word = input ("Please enter a string and you will see if it is a palindrome: ")
# მხოლოდ ასოებს გაითვალისწინებ და ამის მიხედვით დაადგენს პალინდრომობას
only_characters = ""
for i in input_word:
    if i.isalpha():
        only_characters += i

only_characters = only_characters.lower()

reversed_word = ""

for i in range (len(only_characters)-1,-1,-1):
    reversed_word += only_characters[i]
print (f"Reversed: {reversed_word}")
if reversed_word == only_characters:
    print(f"\"{input_word}\" is a palindrome")
else:
    print(f"\"{input_word}\" is not a palindrome")
