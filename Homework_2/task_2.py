print("Please enter the values of num1 and num2 and The program will find out if num1 is a multiple of num2")
num1 = float(input("num1= "))
num2 = float(input("num2= "))
if num1 % num2 == 0:
    print(str(num1), "is a multiple of ", str(num2))
else:
    print(str(num1), "is not a multiple of ", str(num2))

""" 
ეს კოდი ათწილადებზე არ მუშაობს, რადგან მაგალითად 5.5 % 1.1 არ არის 0 ის ტოლი პითონისთვის.
ალტერნატივად შეგვიძლია გამოვიყენოთ is_integer.

print( "Please enter the values of num1 and num2 and The program will find out if num1 is a muptiple of num2")
num1 = float(input("num1= "))
num2 = float(input("num2= "))
quotient = num1 / num2 
if quotient >0 and quotient.is_integer() :    # ნატურალურობის პირობა
    print(str(num1) , "is a multiple of ", str(num2))
else : 
    print(str(num1) , "is not a multiple of ", str(num2))


"""