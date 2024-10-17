from random import randint
rand_num = randint(0,100)
print("Try to guess the number the program has in mind. The number is an integer in range 0-100. You have 10 tries to guess the number.")
attempts_counter = 10
attempt_value = float(input("Please enter your guess : "))
while attempt_value < 0 or attempt_value > 100 or attempt_value % 1 != 0:
    print(f"The number must be an integer in range 0-100, you violated this condition so this attempt is not considered and you still have {attempts_counter} tries")
    attempt_value = float(input("please enter your guess : "))
attempt_value = int(attempt_value)
winner = "Computer"
while attempts_counter > 1:

    if attempt_value == rand_num:
        print(f"You are the winner. The number is {rand_num}")
        winner = "User"
        break

    else:
        attempts_counter -= 1
        if attempt_value > rand_num:
            print(f"Your guess is higher than the number the program has in mind. {attempts_counter} attempts left")
            attempt_value = float(input("Please enter your next guess : "))
            while attempt_value < 0 or attempt_value > 100 or attempt_value % 1 != 0:
                print(f"The number must be an integer in range 0-100, you violated this condition so this attempt is not considered and you still have {attempts_counter} tries")
                attempt_value = float(input("please enter your guess : "))
            attempt_value = int(attempt_value)
        else:
            print(f"Your guess is lower than the number the program has in mind. {attempts_counter} attempts left")
            attempt_value = float(input("Please enter your next guess : "))
            while attempt_value < 0 or attempt_value > 100 or attempt_value % 1 != 0:
                print(f"The number must be an integer in range 0-100, you violated this condition so this attempt is not considered and you still have {attempts_counter} tries")
                attempt_value = float(input("please enter your guess : "))
            attempt_value = int(attempt_value)


if winner == "Computer":
    print(f"You lost. The number was {rand_num}. Computer is the winner")



