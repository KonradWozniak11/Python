aim = int(input('''Co chcesz zrobić?

1. Sprawdzić stężenie alkoholu we krwi
2. Sprawdzić czy mogę prowadzić samochód
3. Koniec  
'''))

if aim == 1:
    procenty = float(input("Podaj zawartość alkoholu w % "))
    ilosc = int(input("Ile tego alkoholu wypiłeś w ml "))
    waga = int(input("Podaj masę ciałą w kg "))
    plec = int(input('''Podaj swoją płeć:
    1 - Mezczyzna
    2 - Kobieta
    '''))
    if plec == 1:
        wspolczynnik = 0.7
    else:
        wspolczynnik = 0.6

    promile_poczatkowe = ilosc * (procenty/100) * 0.8/waga*wspolczynnik
    promile = promile_poczatkowe

    print(f"Po spożyciu takiej ilości alkoholu zawartość alkoholu we krwi wyniesie około {round(promile), 2} promili")

    wykres = int(input('''Czy chcesz zobaczyć jaka będzie Twoja zawartość alkoholu we krwi w czasie?
    1- Tak
    2- Nie
    '''))
    if wykres == 1:
        czas = int(input("Ile godzin ma minąć? "))
        while czas > 0:
            promile = promile_poczatkowe - 0.15*czas
            if promile < 0:
                promile = 0
            print(f"Po upływie {czas} godzin promile wyniosą około {round(promile), 2}")
            czas -= 1

elif aim == 2:
    procenty = float(input("Podaj zawartość alkoholu w % "))
    ilosc = int(input("Ile tego alkoholu wypiłeś w ml "))
    waga = int(input("Podaj masę ciałą w kg "))
    plec = int(input('''Podaj swoją płeć:
    1 - Mezczyzna
    2 - Kobieta
    '''))
    if plec == 1:
        wspolczynnik = 0.7
    else:
        wspolczynnik = 0.6

    promile = ilosc * (procenty/100) * 0.8/waga*wspolczynnik

    if promile <= 0.2:
        print(f"Możesz prowadzić samochód, stężenie alkoholu w twojej krwi wynosi {round(promile), 2} promili")
    else:
        print(f"Nie możesz prowadzić samochodu, stężenie alkoholu w twojej krwi wynosi {round(promile, 2)} promili")


else:
    print("Koniec programu")





