import random
n = float(input("Please enter a positive integer n less than 30, which will be the number of random generated numbers, n = : "))
while n <= 0 or n >= 30 or n % 1 != 0 :
    n = float(input("The number must be more than 0 and less than 30, n = : "))
n = int(n)
maximum = -1
print("The randomly generated numbers are", end=": ")
for i in range (n):
    random_number = random.randint(0,1000)
    print(random_number, end = "  ")
    if random_number > maximum:
        maximum = random_number
print(end="\n")
print( "The maximum from randomly generated numbers is ", maximum)