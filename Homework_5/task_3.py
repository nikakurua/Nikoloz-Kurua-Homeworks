n = float(input("Please enter a non-negative integer n less than 20, and the program will show first n members of Fibonacci sequence, n = : "))
while n < 0 or n >= 20 or n % 1 != 0 :
    n = float(input("The number must be non-negative less than 20, n = : "))
n = int(n)

member_0 = 0
member_1 = 1
counter = 0
if n == 0:
    print ("Zero member of Fibonacci sequence is:",n)
else:
    print( f"First {n} members of Fibonacci sequence : ", end = "")
    while counter <= n:
        print (member_0, end = " ")
        next_member = member_0 + member_1
        member_0 = member_1
        member_1 = next_member
        counter += 1
    print(" ", end = 2*"\n")
    print ( "Comment:", 0,"is a zero member, so start counting of members from 1.")
