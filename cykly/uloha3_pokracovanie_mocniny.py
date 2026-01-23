#Opäť pracujte s predchádzajúcim kódom 
# a upravte ho tak, aby vypísal všetky 
# druhé mocniny podľa zadaných parametrov 
# v rozsahu od a do.  

def mocniny(od, do):
    for i in range(od, do+1):
        print(i**2)

mocniny(2, 6)