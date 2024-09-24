import random
def rounded_random_number():
    print( round(random.random()*1000,1))

if "__main__" == __name__:
    rounded_random_number()
    second_solution = input("Dou you want to see second solution? (yes/no): ")
    if second_solution.lower() == "yes":
        number = random.random() * 1000
        rounded_number = round(number, 1)
        print(rounded_number)
    else :
        print("Okay, thank you for your attention.")