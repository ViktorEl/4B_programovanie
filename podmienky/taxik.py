# vytvorte funkciu cena_za_taxi()
# cena za 1 km je 0.80 centov
# ak prejdeme viac ako 100 km taxikar da zlavu 5%
# ak prejdeme viac ako 200 km kaxikar da zlavu 10%
# ak do taxametra zadame zaporne cislo
# taxameter vrati informáciu: chyba zaporne cislo

def cena_za_taxi(pocet_km):
    if pocet_km < 0:
        return 'chyba zaporne cislo'
    elif pocet_km <= 100:
        cena = pocet_km * 0.80
        return cena