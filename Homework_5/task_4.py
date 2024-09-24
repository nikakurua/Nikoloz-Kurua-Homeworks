n = float(input("Please enter a positive integer n less than 50, and you will see an appropriate Christmas tree, n = : "))
while n <= 0 or n >= 50 or n % 1 != 0 :
    n = float(input("The number must be more than 0 and less than 50, n = : "))
n = int(n)
i = 1
print ( (n-1)*" ","*",sep = "")
while i < n:
    print ((n-1-i) * " ",i * "/","|",i * "\\",sep = "")
    i += 1

print((n-1) * " ","|", sep ="")




