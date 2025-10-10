# Podnikateľ mal v jednom mesiaci príjmy aj výdavky. 
# Na konci mesiaca chce zistiť, aký bol jeho čistý zisk.
# Vytvorte funkciu cisty_zisk(), 
# ktorá prijme hodnoty príjmu a výdavkov a vypíše čistý zisk.

def cisty_zisk(prijmy, vydavky):
    zisk = prijmy - vydavky
    print(zisk)

cisty_zisk(1800, 500)       # zavolanie funkcie