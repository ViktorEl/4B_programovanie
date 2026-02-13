print("---Program na ukážku plánovaného šetrenia---")

def plan_setrenia(pocet_mesiacov,mesacny_vklad):
    for i in range(1,pocet_mesiacov+1):
        print(f"Mesiac {i}: Na účte máte spolu {i*mesacny_vklad} EUR.")

pocet_mesiacov = int(input("Zadajte počet mesiacov: "))
mesacny_vklad = float(input("zadajte vklad: "))
plan_setrenia(pocet_mesiacov, mesacny_vklad)