#Index telesnej hmotnosti (angl. Body Mass Index – BMI) 
# patrí medzi najviac používané metódy merania obezity. 
# Počíta sa ako hmotnosť v kilogramoch delená druhou mocninou
#  výšky v metroch. 
#Vytvorte funkciu pocitaj_bmi() pre výpočet 
# hodnoty indexu BMI. Riešenie uložte do súboru zdravie.py.

def pocitaj_bmi(hmotnost, vyska):
    vypocet_bmi = hmotnost / vyska**2   # **2 mocnina dvojky
    return round(vypocet_bmi,2) # zaokruhlenie na dve desatinne miesta

moje_bmi = pocitaj_bmi(73, 1.80)
print(moje_bmi)
