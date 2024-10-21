# როგორც მივხვდი ორმხრივი უნდა იყოს დამოკიდებულება.
# პირველიდან მეორე უნდა ჩაიწერებოდეს და მეორიდან პირველი.
# ანუ პირველი სტრინგის და მეორე სტრინგის ყველა სიმბოლო უნდა ემთხვეოდეს ერთმანეთს
# უბრალოდ გადანაცვლებული უნდა იყოს ადგილები
print ("Please enter two strings and you will find out if string 2 can be written using only symbols of string 1 ")
string_1 = input("String 1 : ")
string_2 = input("String 2 : ")
is_possible = True
for i in string_2:
    if i not in string_1:
        is_possible = False
        break
    else:
        string_1 = string_1.replace(i,"",1)

if string_1 == "" and is_possible == True:
    print ( "It is possible")
else:
    print("It is not possible")



# თუ მხოლოდ იმის შემოწმება გვინდა პირველის სიმბოლოები საკმარისია თუ არა მეორის ჩასაწერად
# თუნდაც პირველის სიმბოლოები ზედმეტი იყოს ( მაგალითად aaa და a )
# მაშინ ბოლო if იდან წავშლით string_1 == ""-ს