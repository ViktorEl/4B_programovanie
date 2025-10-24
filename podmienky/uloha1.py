#Úloha 1: Zistenie, či je číslo párne alebo nepárne
#Zadanie:
#Napíš program, ktorý:
#1.	Požiada používateľa o zadanie čísla.
#2.	Skontroluje, či je číslo párne alebo nepárne.
#3.	Vypíše výsledok.


def zisti_parnost(cislo):
    if cislo % 2 == 0:
        return 'parne'
    else:
        return 'neparne'

cislo = input('Zadajte cislo:')
cislo = int(cislo)

print(zisti_parnost(cislo))



