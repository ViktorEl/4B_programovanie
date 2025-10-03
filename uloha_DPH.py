#Majiteľ obchodu potrebuje vedieť, koľko bude stáť tovar 
# po pripočítaní 23 % DPH.
#Aby nemusel všetko počítať na kalkulačke, 
#požiadal vás o program.
#Vytvorte funkciu cena_s_dph(), ktorá na vstup/parameter 
# zoberie sumu bez DPH a vypíše sumu s DPH.

def cena_s_dph(suma):               #definovanie funkcie
    vypocet_dph = suma * 1.23       #telo funkcie
    print(vypocet_dph)

cena_s_dph(200)                 # zavolanie funkcie
