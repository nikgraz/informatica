import random
numero1=random.randint(1, 20)
def lancia_dado():
    risultato = random.randint(1, 20)
    return risultato

# Eseguiamo il lancio del dado
print("Risultato del lancio del dado:", lancia_dado())
