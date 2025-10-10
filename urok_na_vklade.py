# Klient vložil peniaze do banky a zaujíma ho, 
# koľko bude mať po roku pri zadanej úrokovej miere.
# Vytvorte funkciu suma_s_urokom(), ktorá na vstup 
# zoberie vklad a úrokovú mieru a vypočíta a vypíše 
# celkovú sumu po roku. 

def suma_s_urokom(vklad, urokova_miera):
    urok = vklad * urokova_miera / 100
    vysledna_suma = urok + vklad
    print(vysledna_suma)

suma_s_urokom(1000, 3)