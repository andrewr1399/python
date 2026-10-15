####Rubrica

rubrica = {"andrea": 3277777, "giacomo": 44444555
}

while True:
    
    print("=== RUBRICA ===")
    print("1. Aggiungi contatto")
    print("2. Cerca contatto")
    print("3. Modifica numero")
    print("4. Elimina contatto")
    print("5. Mostra tutti")
    print("0. Esci")

    scelta = input("Scelta: ")

    if scelta == "1":
        
        nome = input("Nome: ")
        numero = input("Numero: ")
        rubrica[nome] = numero
        print(f"Aggiunto {nome}")

    elif scelta == "2":
        
        nome = input("Nome: ")
        
        if nome in rubrica:
            print(rubrica[nome])
        
        else:
            print("non trovato")

    elif scelta == "3":
        
        nome = input("Nome: ")
        
        if nome in rubrica:
            
            rubrica[nome] = input("Inserisci nuovo numero: ")
            
        else:
            
            print("nome non trovato")

    elif scelta == "4":
        
        nome = input("Nome: ")
        
        if nome in rubrica:
            
            del rubrica[nome]
            
        else:
            
            print("Contatto non trovato")

    elif scelta == "5":
        
        if len(rubrica) > 0:
            
            for nome, numero in rubrica.items():
                print(nome, ":", numero)
        
        else:
            
            print("Rubrica vuota.")

    elif scelta == "0":
        print("Ciao!")
        break

    else:
        print("Scelta non valida")