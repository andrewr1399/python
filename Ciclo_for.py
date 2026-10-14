

import random as rd


tentativi = 0
corr = 0
sbag = 0
    
for i in range(1,6):
        
    a = rd.randint(1,10)
    b = rd.randint(1,10)
    c = rd.choice(["+", "-", "*"])
    
    if c == "+":
        ris = a + b

    elif c == "-":
        ris = a - b

    else:
        ris = a * b
    
    d = None
    while d is None:
    
        try:
            d = int(input(f"Quanto fa:\n\n{a}{c}{b}?"))
        
        except ValueError:
            print("Devi inserire un numero!")

    if d == ris:
        corr = corr + 1
        print(f"Esatto! sei a {corr} risposte corrette")
            
        
    else:
        sbag = sbag + 1
        print(f"No! hai sbagliato {sbag} domande, continua!")
        
    tentativi = tentativi + 1

        
if tentativi == 5:
    print(f"Hai sbagliato {sbag} domande e indovinato {corr} domande")





