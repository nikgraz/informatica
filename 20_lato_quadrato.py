# Chiediamo all'utente di inserire l'area del quadrato
area = float(input("Inserisci l'area del quadrato: "))

# Calcoliamo il lato del quadrato
lato = (area)**0.5

# Stampiamo il lato arrotondato alla prima cifra decimale
print(f"Il lato del quadrato è: {lato:.1f}")
