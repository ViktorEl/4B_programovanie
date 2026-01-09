
def sucet(cislo1, cislo2):
    spolu = cislo1 + cislo2
    if spolu > 100:
        return 'vysledok je vacsi ako sto'
    else:
        return 'vysledok je mensi ako sto'


c1 = input('Zadajte prvé cislo:')
c1 = float(c1)
c2 = input('Zadajte druhé cislo:')
c2 = float(c2)

print(sucet(c1, c2))
