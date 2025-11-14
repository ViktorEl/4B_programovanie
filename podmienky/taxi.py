#Vytvorte funkciu cena_za_taxi(), 
# ktorá vypočíta a vráti cenu za odvoz taxíkom. 
# Vstupný parameter: km
#Cenník taxi služby je nasledovný:
#- štartovné – 1,00 €
#- cena za km – 0,90 €
#- minimálne jazdné – 3,00 €

def cena_za_taxi(km):
    startovne = 1
    cena_za_km = 0.90
    cena_spolu = km * cena_za_km + startovne
    if cena_spolu < 3:
        return 3
    else:
        return cena_spolu

km = input('Zadajte pocet kilometrov:')
km = float(km)

print(cena_za_taxi(km))