# osoba = input ("Koho hodnotíme?")
# znamka = input ("Jakou dostal známku? 1-5")

def hodnoceni(osoba, znamka):
    print(osoba, ' získal/a známku: ', znamka)
     
    if znamka == '1':
        print('Výborně, lépe to nemohlo dopadnou.')
    elif znamka == '2':
        print('Výborně')
    elif znamka == '3':
        print('To je docela dobrý.')
    elif znamka == '4':
        print('To už chtělo začít něco dělat')
    elif znamka == '5':
        print('No to snad ne.')
    else:
        print('Takovou známku já vůbec neznám')
        
hodnoceni('Pavel','2')
 
