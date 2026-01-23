# Vytvorte funkciu celkove_vstupne(), pre obchod Slnko
# ktorý vyberá vstupné týmto spôsobom
# prvý zaplatí 1 euro
# druhý a tretí neplatí nic 
# stvrtý zaplatí 4 eura
# každý tretí zákazník platí vstupné ostatní zakaznici nie
# vytvorte funkciu ktorá vráti celkové vstupne ak do 
# obchodu prislo n zakaznikov

def celkove_vstupne(n):
    suma_spolu = 0
    for i in range(1, n+1, 3):
        suma_spolu = suma_spolu + i
    return suma_spolu
