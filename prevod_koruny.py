#Študent cestuje na brigádu do Česka a potrebuje si
#  prepočítať, koľko českých korún dostane za svoje eurá.
#Kurz je 1 € = 25 Kč.
#Vytvorte funkciu prevod_na_koruny(), ktorá na vstup 
# zoberie sumu v eur a vypočíta a vypíše sumu v českých 
# korunách. 

def prevod_na_koruny(suma_v_eur):
    prevod = suma_v_eur * 25
    print(prevod)

suma = input('Zadajte svoju sumu v eurach:')
suma = float(suma)

prevod_na_koruny(suma)