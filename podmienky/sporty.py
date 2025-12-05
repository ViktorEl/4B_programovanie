# Vytvorte funkciu urci_sport
# Urci sport podla pohlavia a vysky
# ak muz nad 180 cm - basketbal
# ak muz 180 cm a menej - futbal
# ak zena nad 170 cm - basketbal
# ak zena 170 a menej - futsal
# ak zadame zaporne cislo tak funkcia vyhodi
# chybovú hlasku: chyba zadali ste zaporne cislo

def urci_sport(pohlavie, vyska):
    if vyska < 0:
        return 'chyba zadali ste zaporne cislo'
    elif pohlavie == 'muz' and vyska > 180:
        return 'basketbal'
    elif pohlavie == 'muz' and vyska <= 180:
        return 'futbal'