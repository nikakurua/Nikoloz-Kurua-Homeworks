n = float(input("Please enter a positive integer n less than 10,  n = : "))
while n <= 0 or n >= 10 or n % 1 != 0 :
    n = float(input("The number must be a positive integer less than 10, n = : "))
n = int(n)

i = 1
while i <= n:

    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    i += 1
    print(end="\n")

i = i - 2

while i >= 1:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    i -= 1
    print(end="\n")


