#Pomôžte učiteľovi vytvoriť program, 
# ktorý mu uľahčí známkovanie žiakov. 
#Vytvorte funkciu premen_na_znamku(), 
#ktorá na vstup zoberie dosiahnuté percentá 
#a vráti príslušnú známku. 
#<90, 100>	1
#<75, 90)	2     
#<55, 75)	3     
#<40, 55)	4    
#(40, 0>	5      

def premen_na_znamku(percento):
    if percento >= 90 and percento <= 100:
        return 1
    elif percento >= 75 and percento < 90:
        return 2