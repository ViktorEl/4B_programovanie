#Vytvorte funkciu dospelost(), 
# ktorá pre zadaný vek vráti či už bola dosiahnutá 
# dospelosť alebo nie. 

def dospelost(vek):
    if vek >= 18:
        return 'dospely'
    else:
        return 'neplnolety'

vek = input('Zadajte svoj vek:')
vek = int(vek)

print(dospelost(vek))