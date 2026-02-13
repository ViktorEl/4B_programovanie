print("---Program prehľadu teplôt---")

def teplotna_stupnica(start_teplota, koniec_teplota, krok):
    for i in range(start_teplota, koniec_teplota+1, krok):
        fahrenheit = (i * 9/5) + 32
        print(f'Stupne Celzia {i}, Stupne Fahrenheit {fahrenheit}')

start_teplota = input('Zadajte zaciatok teploty:')
start_teplota = int(start_teplota)
koniec_teplota = int(input('Zadajte koniec teploty:'))
krok = int(input('Zadajte krok:'))

teplotna_stupnica(start_teplota, koniec_teplota, krok)

