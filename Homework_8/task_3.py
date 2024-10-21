from datetime import datetime
input_date = input("Please enter a date: " )

format_check = datetime.fromisoformat(input_date) #თუ არასწორ ფორმატში იქნება valueerror ით შეწყდება პროგრამა
input_date = format_check. isoformat()

output = input_date[8:10] + "-" +input_date[5:7] + "-" + input_date[0:4] + " " + str(int(input_date[11:13]) % 12) + input_date[13:19] + " " + input_date[-6] + input_date[-4]
print (output)




