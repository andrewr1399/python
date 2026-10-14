
 ###Funzione_per_analizzare_password

def analizza(passwd):
    """
    Analizza la password fornita e restituisce un punteggio di sicurezza.
    
    Parametri:
    passwd: La password da analizzare.
    
    Ritorna:
    Punteggio di sicurezza della password.
    """
    punteggio = 0
    
    # Controllo lunghezza
    if len(passwd) >= 8:
        punteggio += 20

    if len(passwd) >= 12:
        punteggio += 20
    
    # Controllo presenza di lettere maiuscole
    ha_maiuscola = False
    for c in passwd:
        if c.isupper():
            ha_maiuscola = True
            punteggio += 20
            break
    
    # Controllo presenza di lettere minuscole
    ha_minuscola = False
    for c in passwd:
        if c.islower():
            ha_minuscola = True
            punteggio += 20
            break

    # Controllo presenza di numeri
    ha_numero = False
    for c in passwd:
        if c.isdigit():
            ha_numero = True
            punteggio += 10
            break
    
    # Controllo presenza di caratteri speciali
    ha_speciale = False
    for c in passwd:
        if not c.isalnum() and not c.isspace():
            ha_speciale = True
            punteggio += 10
            break
        
    return punteggio

###Chiamo_funzione

passwd = input("Inserisci la tua password da analizzare: ")
punteggio = analizza(passwd)
print(f"La tua password ha un punteggio di sicurezza di: {punteggio} su 100.")