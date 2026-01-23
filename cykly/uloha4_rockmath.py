def celkove_vstupne(pocet_zakaznikov):
    sucet = 0
    for i in range(1, pocet_zakaznikov+1, 2):
        sucet = sucet + i
    return sucet

print(celkove_vstupne(7))