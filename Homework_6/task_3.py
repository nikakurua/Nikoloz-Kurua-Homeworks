print("Please enter a non-negative integer n less than 10000, and the program will show the reversed number and the sum of digits of the number" )
n = float(input("n = : "))
while n < 0 or n >= 10000 or n % 1 != 0 :
    n = float(input("The number must be non-negative integer less than 1000, n = : "))
n = int(n)
initial_number = n

max_degree_of_10 = 0
while n / 10 ** max_degree_of_10 > 10:
    max_degree_of_10 += 1

sum_of_digits = 0
reversed_number = 0
i = 0
while i <= 9:
    if max_degree_of_10 < 0:
        break
    if (n - i) % 10 == 0:
        n = (n-i) / 10
        sum_of_digits += i
        reversed_number += i * 10 ** max_degree_of_10
        max_degree_of_10 -= 1
        i = 0
    else: i += 1

print(f"Reversed number is {reversed_number}")
print (f"Sum of digits is {sum_of_digits}")

if initial_number == reversed_number:
    print( "The number you entered is a palindrome. The reversed number is same as the initial number " )

# მეორე ამოხსნა
# print("Please enter a non-negative integer n less than 10000, and the program will show the reversed number and the sum of digits of the number" )
# n = float(input("n = : "))
# while n < 0 or n >= 10000 or n % 1 != 0 :
#     n = float(input("The number must be non-negative integer less than 1000, n = : "))
# n = int(n)
# sum_of_digits = 0
# i = 0
# print("Reversed number is ", end = "")
# while i <= 9:
#     if n == 0:
#         break
#     if (n - i) % 10 == 0:
#         n = (n-i) / 10
#         sum_of_digits += i
#         print(i, end = "")
#         i = 0
#     else: i += 1
# print("")
# print (f"Sum of digits is {sum_of_digits}")











