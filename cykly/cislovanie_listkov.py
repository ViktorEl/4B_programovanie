print("---Program na číslovanie lístkov---")

def generuj_listky(od_cisla, do_cisla):
    for i in range(od_cisla,do_cisla+1):
        print(f"číslo {i}")
        
od_cisla = int(input("Zadajte číslo:"))
do_cisla = int(input("Zadaj druhé číslo:"))

generuj_listky(od_cisla, do_cisla)
