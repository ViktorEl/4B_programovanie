
def vypocet_cennika(start_cena, koniec_cena, krok):
    for i in range(start_cena, koniec_cena+1, krok):
        print(i * 1.23)

vypocet_cennika(10, 20, 2)