#Sochár má v úmysle vytvoriť dielo, 
# v ktorom použije niekoľko dutých kociek. 
# Dutú kocku vytvorí tak, že do formy v 
# tvare kocky vloží menšiu kocku a priestor medzi 
# dvoma kockami zaleje betónom. Pomôžte sochárovi 
# vypočítať, koľko m3 betónu bude potrebovať na 
# dutú kocku a definujte funkciu objem_dutej_kocky() 
# na výpočet množstva betónu v dutej kocke.
#Koľko m3 bude sochár porebovať, ak väčšia kocka má 
# hranu dĺžky 1,125 m a menšia kocka hranu dĺžky 0,95 m?
#Premyslite si, či a ako sa sa dajú využiť vami definované funkcie.

def objem_kocky(strana_a):
    objem = strana_a * strana_a * strana_a
    return objem

#print(objem_kocky(5))

def objem_dutej_kocky(dlzka_velkej_kocky, dlzka_malej_kocky):
    objem_velkej_kocky = objem_kocky(dlzka_velkej_kocky) # zavolanie predchadzajucej funkcie
    objem_malej_kocky = objem_kocky(dlzka_malej_kocky)
    objem_dutej = objem_velkej_kocky - objem_malej_kocky
    return objem_dutej

print(objem_dutej_kocky(5, 3))