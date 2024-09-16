
speed = float(input("Please enter the value of the speed of the car: "))
if speed < 0:
    print("The value of the speed can not be negative, since speed is scalar not, vector." )
elif speed == 0:
    print("The car is not moving.")
else:
    if speed < 30 :
        print( " The category of the speed is SLOW")
    elif speed > 120 :
        print(" The category of the speed is VERY FAST")
    elif speed > 60 :
        print(" The category of the speed is FAST")
    else :
        print(" The category of the speed is MODERATE")
# რადგან 30 კმ/სთ ს შემთხვევაშ კატეგორიაა არაა მოცემული პირობაში(30 ზე ნაკლები SLOW და 30 ზე მეტი MODERATE , თუმცა თვითონ 30 ზე არ არის პირობა), დავუშვი რომ ეს სიჩქარე გადის MODERATE კატეგორიაში
