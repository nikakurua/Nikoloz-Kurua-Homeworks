print("Enter an integer between 0-10 nad the program will return all prime divisors of the integer")
input_value = int(input("input_value = "))   # ათწილადების შეყვანის შემთხვევაში int ად ვერ გადაკეთდება შეტყვანილი ტექსტი.
if input_value < 0 or input_value > 10:
    exit(1)
else:
    if input_value % 2 == 0:
        prime_number1 = "2"
    else:
        prime_number1 = ""

    if input_value % 3 == 0:
        prime_number2 = "3"
    else:
        prime_number2 = ""

    if input_value % 5 == 0:
        prime_number3 = "5"
    else:
        prime_number3 = ""

    if input_value % 7 == 0:
        prime_number4 = "7"
    else:
        prime_number4 = ""

    print("Prime divisors of",str(input_value),"are(is)",prime_number1,prime_number2,prime_number3,prime_number4)
