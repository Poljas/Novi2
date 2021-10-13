def prestupna_godina(godina):
    # godina = int(godina)
    
    if godina > 2021:
        print("Godina je van zadatog opsega!")
        return
    x = godina%4
    if x == 0:
        print(f"{godina} je prestupna godina.")
    else:
        print(f"{godina} nije prestupna godina.")

#############################################################
godina = ""
while type(godina) != int:
    godina = input("Unesite godinu:\n")
    try:
        print(f"Pokusavam da prebacim {godina} u broj")
        godina = int(godina)
        print(f"Uspesno sam prebacio {godina} u broj")
    except:
        print(f"Passing zato sto nije mogao da promeni {godina} u broj")
        pass

prestupna_godina(godina)
 