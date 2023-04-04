while True:
    print("1- dodawanie, 2 odejmowanie, 3- mnożenie, 4-dzielenie, q- wyjście")

    choice = input("Co chcesz zrobic")
    if choice =="q":
        print("Koniec")
        break
    if choice not in["1","2","3","4"]:
        print("Zly wybor")
    else:
        a = int(input("Podaj a"))
        b = int(input("Podaj b"))
        if choice == "1":
            print(f"Wynik dodawania {a} i {b} to {a+b}")
        if choice == "2":
            print(f"Wynik odejmowania {a} i {b} to {a-b}")
        if choice == "3":
            print(f"Wynik mnozenia {a} i {b} to {a*b}")
        if choice == "4":
            if b!=0:
                print(f"Wynik dzielenia {a} i {b} to {a * b}")
            else:
                print("Nie dziel przez 0")
