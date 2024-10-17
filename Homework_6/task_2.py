# The Collatz Conjecture რომლის მიხედვითაც ყოველთვის ერთამდე მიდის რიცხვი ამ ალგორითმით.
print("Please enter a positive integer n not more than 1000, and you will see how this number will go to 1 according to the Collatz Conjecture" )
n = float(input("n = : "))
while n <= 0 or n > 1000 or n % 1 != 0 :
    n = float(input("The number must be more than 0 and not more than 1000, n = : "))
n = int(n)
print(n,end = " -> ")
while n > 1:
    if n % 2 == 0:
        n = int(n/2)
        if n == 1:        # ეს იმისათვის , რომ ბოლოს 1 ის მერე " -> " სიმბოლო არ გვქონდეს.
            print(n)
        else : print(n,end = " -> ")
    else:
        n = int(3*n +1)
        if n == 1:
            print(n)
        else : print(n,end = " -> ")



