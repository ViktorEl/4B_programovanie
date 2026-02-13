print('---Program na harmonogram revízií---')

def harmonogram_revizii(dni_v_mesiaci, interval):
    if dni_v_mesiaci < 0 or dni_v_mesiaci > 31:
        print('Neplatne dni v mesiaci')
        return
    for i in range(1, dni_v_mesiaci+1, interval):
        print(f'Reviziu bude potrebne vykonávat v dni {i}.')

dni_v_mesiaci = int(input('Zadajte dni v mesiaci:'))
interval = int(input('Zadajte interval:'))

harmonogram_revizii(dni_v_mesiaci, interval)