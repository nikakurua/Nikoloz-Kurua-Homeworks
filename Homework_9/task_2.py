import math
import random
n = float(input(" PLease enter a positive integer n more than 1: n = "))
while n <= 1 or n % 1 != 0 :
    n = float(input("The number must be more than 1 and integer, n = : "))
n = int(n)
counter = 0
for i in range(n):
    while True:
        a = random.random()   # ნულზე მკაცრად მეტი რომ იყო რიცხვი ამიტომ გამოვიყენე ეს ციკლი.
        if a != 0:
            break
    while True:
        b = random.random()
        if b != 0:
            break
    if math.sqrt(a**2 + b**2 ) <= 1:
        counter += 1


print (4 * counter / n)

# მიისწრაფის პისკენ. Monte-Carlo