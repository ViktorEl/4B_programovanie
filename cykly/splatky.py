
def generuj_splatky(pocet_mesiacov, vyska_splatky):
    for i in range(1, pocet_mesiacov+1):
        print(f'{i}. mesiac {i * vyska_splatky}')

generuj_splatky(10, 20)