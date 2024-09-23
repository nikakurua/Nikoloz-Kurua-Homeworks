# Fibonacci <3

n = float(input("Please enter a non-negative integer n less than 20, n = : "))
while n < 0 or n >= 20 or n % 1 != 0 :
    n = float(input("The number must be more than 0 and less than 30, n = : "))
n = int(n)
num_0 = 0
num_1 = 1
print("Fibonacci sequence: 1 ", end = " ")
for i in range (0,n-1):
    value = num_0 + num_1
    num_0 = num_1
    num_1 = value
    print(value, end = "  ")
print(end = "\n")
print( "The",n,"th member of Fibonacci sequence is", value)



