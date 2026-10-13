#GIOCO_FUNZIONE#

def gioco(numero):
    tentativi = 0
    numero_utente = 0
    
    while numero_utente != numero:

        try:
            numero_utente = int(input("Inserisci numero da 1 a 100: "))

        except ValueError:
            print("Devi inserire un numero intero!")
            continue

        tentativi += 1

        if numero_utente == numero:
            print("Esatto!")
            break
    
        elif numero_utente < numero:
            print("Troppo basso!")
            
    
        else:
            print("Troppo alto!")
      
    print(f"Esatto! hai impiegato {tentativi} tentativi")
    return tentativi
    

#GIOCO#
import random
game = gioco(random.randint(1, 100))
    