#Mladý manželský pár si zobral pôžičku a potrebuje vedieť, 
# aká bude ich mesačná splátka, ak sa dlžná suma rozdelí 
# rovnomerne medzi jednotlivé mesiace.
#Vytvorte funkciu splatka(), ktorá na vstup zoberie 
#celkovú sumu pôžičky a počet mesiacov splácania a 
#vypočíta a vypíše výšku mesačnej splátky.

def splatka(suma_pozicky, pocet_mesiacov):
    mesacna_suma = suma_pozicky / pocet_mesiacov
    print(mesacna_suma)

splatka(1000, 10)