def kalkulacka(cislo1, operator, cislo2):
    if operator == "+":
        return cislo1 + cislo2
    elif operator == "-":
        return cislo1 - cislo2
    elif operator == "*":
        return cislo1 * cislo2
    elif operator == "/":
        if cislo2 == 0:
            return 'Nulou sa nedá deliť'
        return cislo1 / cislo2
    else:
        return "Prepacte pouzili ste zly operator, opravte si chybu"
    
print(kalkulacka(5,"/",0))   








