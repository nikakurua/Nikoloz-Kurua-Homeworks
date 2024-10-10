a = 1
while a <= 9:
    print()
    b = 1
    while b <= a:
        if b == 3  and ( a == 3 or a == 4):     # ეს ხაზში გასასწორებლად
            print(f" {b} * {a} = {a*b} ", end = "  ")
        else: print(f"{b} * {a} = {a*b} ", end = "  ")
        b += 1
    a += 1


