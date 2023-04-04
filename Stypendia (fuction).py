lista_studentow = [(135606, 'Szymon Mazur'), (199646, 'Piotr Kaźmierczak'), (193018, 'Szymon Mazur'), (179776, 'Beata Piotrowicz'), (109306, 'Dorota Pietrzak'), (155664, 'Beata Mazur'), (136236, 'Anna Borek'), (192637, 'Jan Kowal'), (194512, 'Szymon Kwiatek'), (141475, 'Beata Kaźmierczak'), (118079, 'Adam Kowal'), (188187, 'Anna Kwiatek'), (155312, 'Szymon Mazur'), (173248, 'Adam Nowak'), (155324, 'Adam Piotrowicz'), (165536, 'Wanda Józefowicz'), (138595, 'Jan Mazur'), (177995, 'Szymon Borek'), (105620, 'Piotr Borek'), (181979, 'Ewa Kwiatek'), (136062, 'Adam Pietrzak'), (131403, 'Jan Borek'), (141108, 'Ewa Kowal'), (144902, 'Piotr Kowal'), (117483, 'Piotr Kwiatek'), (178959, 'Beata Borek'), (189950, 'Jan Piotrowicz'), (189792, 'Jan Borek'), (177877, 'Wanda Marczak'), (102684, 'Adam Kowal')]
miesieczna_kwota_stypendium = 700
wartosc_progowa = 4.0
lista_wynikow_sesji = [(135606, [4.0, 4.0, 5.0, 4.0, 5.0, 3.5, 4.0]), (199646, [4.0, 3.0]), (193018, [4.5, 4.0, 5.0, 4.5]), (179776, [3.5, 5.0, 3.0]), (109306, [4.5, 4.5, 5.0, 4.0, 4.0, 3.0]), (155664, [5.0]), (136236, [4.5, 4.5]), (192637, [3.0, 3.0, 4.0, 4.0, 4.0, 3.5, 5.0]), (194512, [3.0]), (141475, [3.0, 3.5]), (118079, [4.0, 5.0, 3.5, 5.0, 4.0, 3.5, 3.0]), (188187, [5.0, 4.5]), (155312, [4.0, 4.0, 3.0, 4.5, 4.5, 4.0]), (173248, [3.0, 5.0, 4.0, 4.0, 3.0]), (155324, [4.5, 4.0]), (165536, [3.5]), (138595, [3.0, 3.0, 3.0]), (177995, [5.0, 5.0, 4.5, 4.0]), (105620, [5.0, 3.0, 4.5, 4.5]), (181979, [4.0, 5.0, 3.0, 5.0, 5.0, 3.0, 3.0])]

def stypendia(lista_studentow, miesieczna_kwota_stypendium, wartosc_progowa, lista_wynikow_sesji):
    stypendialisci = []
    for student in lista_studentow:
        id_studenta = student[0]
        nazwisko_studenta = student[1]
        wyniki_studenta = [wyniki[1] for wyniki in lista_wynikow_sesji if wyniki[0] == id_studenta]
        if len(wyniki_studenta) >= 1:
            srednia = sum(wyniki_studenta[0]) / len(wyniki_studenta[0])
            srednia_2_po_przecinku = round(srednia, 2)
            if len(wyniki_studenta[0]) >= 2 and srednia > wartosc_progowa:
                stypendialisci.append((nazwisko_studenta, f'{miesieczna_kwota_stypendium} zł przy średniej ocen {srednia_2_po_przecinku}'))
    return stypendialisci


print(stypendia(lista_studentow, miesieczna_kwota_stypendium, wartosc_progowa, lista_wynikow_sesji))


