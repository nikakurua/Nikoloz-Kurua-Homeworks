from forex_python.bitcoin import BtcConverter
import datetime
print("Please enter the date when you bought Bitcoin")
year = int(input("Year: "))
month = int(input("month (in number) : "))
day = int(input("Day as a number of month: "))
date = datetime.datetime (year,month, day, 13)
paid_money = float(input("How much did you pay ( in dollars)? :"))

b = BtcConverter()
bought_btc = b.convert_to_btc_on(paid_money, 'USD', date)
value_now_usd = b.convert_btc_to_cur(bought_btc, 'USD')

profit = value_now_usd - paid_money

if profit >= 0:
    print ( " Your profit is", profit, "$")
else :
    print( " Your loss is ", -profit, "$")
# არ აქვს საკმარისი მონაცემები 

