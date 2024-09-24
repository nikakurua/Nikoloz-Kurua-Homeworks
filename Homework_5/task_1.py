n = float(input("Please enter a positive integer n less than 50, and the program will show first three divisors of numbers from 1 to n, n = : "))
while n <= 0 or n >= 50 or n % 1 != 0 :
    n = float(input("The number must be more than 0 and less than 50, n = : "))
n = int(n)

a = 1
divisors_counter = 0

while a <= n:
    if divisors_counter == 1:
        print("- Neither Prime nor Positive",)
    elif divisors_counter == 2:
        print("- Prime number", )
    elif divisors_counter > 2:
        print("- Composite number",)
    divisors_counter = 0
    print(a,"-",end = " ")
    i = 1
    while i <= a:
        if a % i == 0:
            print(i, end = " ")
            divisors_counter += 1
        if divisors_counter == 3:
            break
        i += 1
    a += 1

if divisors_counter == 1:     #  ეს ბოლო რიცხვი მარტივია თუ შედგენილი, რომ დაგვიწეროს
    print("- Neither Prime nor Positive", )
elif divisors_counter == 2:
    print("- Prime number", )
else:
    print("- Composite number", )



