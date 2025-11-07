
def vekova_kategoria(vek):
    if vek <= 1:
        return 'novorodenec'
    elif vek <= 3:
        return 'mladsi predskolsky vek'
    elif vek <= 6:
        return 'starsi predskolsky vek'
    elif vek <= 11:
        return 'mladsi skolsky vek'
    elif vek <= 15:
        return 'stredny skolsky vek'
    elif vek <= 17:
        return 'starsi skolsky vek'
    elif vek <= 64:
        return 'dospelost'
    else:
        return 'staroba'
    
vek = input('Napiste vek:')
vek = int(vek)

print(vekova_kategoria(vek))
