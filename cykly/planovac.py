

def volne_dni(pocet_dni_mesiaca, interval):
    for i in range(interval, pocet_dni_mesiaca+1, interval):
        print(f'Volny termin {i}. den')

pocet_dni_mesiaca = int(input('Zadajte pocet dni v mesiaci:'))
interval = int(input('zadajte interval:'))

volne_dni(pocet_dni_mesiaca, interval)