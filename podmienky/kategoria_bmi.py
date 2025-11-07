# bmi < 18,5			podvýživa
# 18,5 <= bmi < 25		ideálna, zdravá hmotnosť
# 25 <= bmi < 30		nadváha
# 30 <= bmi < 40		obezita
# 40 <= bmi			    ťažká obezita

def kategoria_bmi(vaha, vyska):
    vypocet_bmi = vaha / vyska**2
    if vypocet_bmi < 18.5:
        return 'podvyziva'
    elif vypocet_bmi < 25:
        return 'ideal'
    elif vypocet_bmi < 30:
        return 'nadvaha'
    elif vypocet_bmi < 40:
        return 'obezita'
    else: 
        return 'tazka obezita'

hmotnost = input('Zadajte hmotnost')
hmotnost = float(hmotnost)
vyska = input('Zadajte vysku v metroch:')
vyska = float(vyska)

print(kategoria_bmi(hmotnost, vyska))



    

