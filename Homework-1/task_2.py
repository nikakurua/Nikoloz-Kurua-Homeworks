name=input("შეიყვანეთ თქვენი სახელი:")

birthyear=input("შეიყვანეთ თქვენი დაბადების წელი:")

t=input( "წელს გქონდათ უკვე დაბადების დღე? ( კი/არა): ")

if t=="კი":
    age=2024-int(birthyear)
else: age=2023-int(birthyear)

print("გამარჯობა, "+name+", თქვენ ხართ "+str(age)+" წლის.")