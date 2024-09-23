n = float(input("Please enter a positive integer n less than 1000, and the program will return the divisors of the number, n = : "))
while n <= 0 or n >= 1000 or n % 1 != 0 :
    n = float(input("The number must be more than 0 and less than 30, n = : "))
n = int(n)
print ("The divisors of",n, "are: ")
for i in range (1,n+1):
    if n % i == 0:
        print(i, end= " ")


