
def priestupny_rok(rok):
    if rok % 4 == 0 and rok % 100 > 0 or rok % 4 == 0 and rok % 100 and rok % 400 == 0:
        return True
    else:
        return False
    
print(priestupny_rok(2024))