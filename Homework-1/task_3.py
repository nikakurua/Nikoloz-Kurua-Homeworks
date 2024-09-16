print("Please enter the values of the sides of the triangle in centimeters")

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

perimeter=a+b+c
p=perimeter/2

area=(p*(p-a)*(p-b)*(p-c))**(1/2) # ჰერონის ფორმულა <3
print("The perimeter of the triangle equals to "+str(perimeter)+" cm. The are of the triangle is "+str(area)+" square cm.")
