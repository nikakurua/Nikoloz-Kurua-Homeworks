import random
def random_card():
    colour_options = ["clubs_(♣)", "diamonds_(♦)", "hearts(♥)","spades(♠)"]
    colour = random.choice(colour_options)
    value_options = ["2","3","4","5","6","7","8","9","10","Ace","Jack","Queen","King"]
    value = random.choice(value_options)
    print (" Your random card is ", value, "of", colour, )

if "__main__" == __name__:
    random_card()
