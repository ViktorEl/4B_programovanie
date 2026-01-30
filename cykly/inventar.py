def oznacenie_regalov(cislo_od, cislo_do):
    for i in range(cislo_od, cislo_do+1):
        print(i)

print('vitajte v aplikacii na oznacovanie regalov')

cislo_od = input('Zadajte cislo od:') # pozor zadane cislo bude ako slovo, takze to musíme pretypovat
cislo_od = int(cislo_od)
cislo_do = int(input('Zadajte cislo do:')) # priame pretypovanie vstupu


oznacenie_regalov(cislo_od, cislo_do)
