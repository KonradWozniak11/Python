import json
import datetime
import numpy as np

def kursy(plik):
    slownik ={}
    with open(plik, "r") as Kursy:
        for linia in Kursy:
            values = linia.strip().split("\t")
            if len(values) == 4:
                data, kurs, zmiana, nazwa = map(str.strip, values)
                slownik[data] = {"kurs": kurs, "zmiana": zmiana, "nazwa": nazwa}
    return slownik


EUR = kursy("C:/Users/konra/OneDrive/Desktop/PracaDomowa/EUR.txt")
GBP = kursy("C:/Users/konra/OneDrive/Desktop/PracaDomowa/GBP.txt")
JPY = kursy("C:/Users/konra/OneDrive/Desktop/PracaDomowa/JPY.txt")
CHF = kursy("C:/Users/konra/OneDrive/Desktop/PracaDomowa/CHF.txt")
USD = kursy("C:/Users/konra/OneDrive/Desktop/PracaDomowa/USD.txt")

def Substring(record, start_index, end_index, alpha):
    substring = ''
    for char in record[start_index:end_index]:
        if (alpha and char.isalpha()) or (not alpha and char.isnumeric()):
            substring += char
        else:
            break
    return substring

def pozyczki(data_path):
    lista = []
    with open(data_path, "r", encoding="utf8") as dane:
        for record in dane:
            name_substring_index = record.index('Imiona=') + len('Imiona=')
            surname_substring_index = record.index('Nazwisko=') + len('Nazwisko=')
            kurs_substring_index = record.index('Kwota=') + len('Kwota=')

            name = Substring(record, name_substring_index, len(record), True)
            surname = Substring(record, surname_substring_index, len(record), True)
            kurs = Substring(record, kurs_substring_index, len(record), False)

            currency_start_index = record.index('<') + 1
            currency_end_index = record.index('>')
            currency = record[currency_start_index:currency_end_index]

            date_index_start = record.index('#') + 1
            date = record[date_index_start:date_index_start+10]

            lista.append([date, name, surname, kurs, currency])
    return lista

zmienne = pozyczki("C:/Users/konra/OneDrive/Desktop/PracaDomowa/dane106.txt")

tablica = np.array(zmienne)

tablica_koncowa = []
WALUTY = {'CHF': CHF, 'EUR': EUR, 'USD': USD, 'GBP': GBP, 'JPY': JPY}

for wiersz in tablica:
    data = wiersz[0]
    kwota = float(wiersz[3])
    waluta = wiersz[4]

    if waluta in WALUTY:
        kurs = float(WALUTY[waluta].get(data, {}).get("kurs", 0))
        if kurs != 0 and datetime.datetime.strptime(data, "%Y-%m-%d"):
            wynik = kwota * kurs
            imie = wiersz[1]
            nazwisko = wiersz[2]
            tablica_koncowa.append((imie, nazwisko, data, wynik))
    else:
        print("Nieodpowiednie dane")
        continue

print(tablica_koncowa)

with open("wyniki3.json", "w", encoding="utf8") as file:
    json.dump(tablica_koncowa, file, ensure_ascii=False)
