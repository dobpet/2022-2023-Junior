# user_name = input ("What is your name? ")

# while user_name != "Clark Kent":
#     print("You are not Superman - try again!")
#     user_name = input("What is your name? ")
# print("You are Superman!")

print("Budeme hledat zvíře")
#dotaz slona
vstup = input ("Má chobot? (ano/ne)")
if (vstup == "ano"):
    vstup = input ("Má dlouhou srst? (ano/ne)")
    if (vstup == "ano"):
        print("Je to mamut")
        exit()
    else:
        print("Je to slon")
        exit()
else:
    print("Tak slon, ani mamut, to není")

#dotaz na žirafu
vstup = input ("Má dlouhý krk? (ano/ne)")
if (vstup == "ano"):
    print("Je to žirafa")
    exit()
else:
    print("Tak žirafa to není")
        
        
print("konec hledání. Nevím, o jaké se jedná zvíře.")