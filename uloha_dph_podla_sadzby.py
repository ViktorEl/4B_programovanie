# Vytvorte funkciu cena_s_dph(), 
#ktorá na vstup zoberie cenu bez DPH a sadzbu (v %) 
# a vypíše konečnú cenu s DPH.

# nazov funkcie cena_s_dph()
# parametre: cena_bez_dph, sadzba
# vystup: vypocet/cena_s_dph

def cena_s_dph(cena_bez_dph, sadzba):
    vypocet_dph = sadzba * cena_bez_dph / 100
    suma_s_dph = vypocet_dph + cena_bez_dph
    print(suma_s_dph)

cena_s_dph(200, 23)