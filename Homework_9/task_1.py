# ლეიბნიცის ფორმულა , ტეილორის სერიებით ჩაწერა arctan 1. <3   უსასრულო ჯამი გვაძლევს პის.
print("Please enter a positive integer n more than 1 and you will see approximation of 4*arctan(1) by taylor series. Using first n members. ")
n = float(input("n = "))
while n <= 1 or n % 1 != 0 :
    n = float(input("The number must be more than 1 and integer, n = : "))
n = int(n)
x = 0
for i in range(1,n+1):
    x += 4 * ((-1) ** (i+1) / (2 * i - 1))
print( f"4 * arctan(1) = {x} approximately")

#ვამჩნევთ რომ ეს რიცხვი მიისწრაფის პისკენ
