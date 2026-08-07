
lista = []

scelta = "r"

while scelta != "4":
    
    scelta = input("\nDigitare un numero:\n\n1. Aggiungi prodotto\n2. Visualizza lista\n3. Elimina prodotto\n4. Esci\n\nScelta: ")
    
    if scelta == "1":
        prodotto = input("\nInserire prodotto: ")
        lista.append(prodotto)
        
    elif scelta == "2":
        contatore = 1
        for i in lista:
            print(f"\n{contatore}. {i}")
            contatore += 1
            
    elif scelta == "3":
        prodotto = input("\nInserire prodotto da rimuovere: ")
        
        if prodotto not in lista:
            print("Non presente")
            
        else:
            lista.remove(prodotto)

    elif scelta == "4":
        print("Uscita in corso...")
        break
        
    else:
        print("Scelta non valida")
        