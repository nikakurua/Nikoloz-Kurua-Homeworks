import random
number_of_players = float(input("Please enter the number of players: "))
while number_of_players <= 0 or number_of_players % 1 != 0:
    number_of_players = float(input("Please enter a positive integer: "))
number_of_players = int (number_of_players)
for i in range (number_of_players):
    rand_1 = random.randint(1,6)
    rand_2 = random.randint(1,6)
    if rand_1 == rand_2:
        if rand_1 == 6:
            print("The couple of dices for player", i, "is",rand_1, rand_2, "You're very very lucky")
        else:print("The couple of dices for player", i, "is", rand_1, rand_2, "You're lucky")
    else:print("The couple of dices for player", i, "is",rand_1, rand_2,)