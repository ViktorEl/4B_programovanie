

def celkova_cena_nakupu(suma, typ_klienta):
    if suma < 100:
        return suma
    elif suma > 100 and suma <= 200 and typ_klienta == 'VIP':
        suma = suma * 0.90
    elif suma > 100 and suma <= 200 and typ_klienta == 'Klasik':
        suma = suma * 0.95
    

    return suma