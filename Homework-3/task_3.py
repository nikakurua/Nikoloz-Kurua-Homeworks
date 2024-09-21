import datetime
# არასწორ ცვლადებს, ვთქვათ თვე 14 ან დღე 44 თვითონ ფუნქცია დააერორებს.
def weekday_of_birthday():
    birth_year = int(input( "Please enter your birth year:"))
    birth_month = int(input("Please enter the number of your birth month: "))
    birth_day = int(input("Please enter the number of the day you were born on: "))
    birth_date = datetime.date(birth_year,birth_month,birth_day)
    week_day = birth_date.strftime("%A")
    print("You were born on ",week_day)

if "__main__" == __name__:
    weekday_of_birthday()
