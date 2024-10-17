n = float(input("Please enter a positive integer n less than 10,  n = : "))
while n <= 0 or n >= 10 or n % 1 != 0 :
    n = float(input("The number must be a positive integer less than 10, n = : "))
n = int(n)

k = 0
while k <= n:
    print(2 * (n - k) * " ", sep="", end=" ")

    i = k
    while i >= 0:
        print(i, end=" ")
        i -= 1

    i += 2

    while i <= k:
        print(i, end=" ")
        i += 1
    k += 1
    print("", end="\n")