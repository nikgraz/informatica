import random
import math

# Genera un numero pseudocasuale tra 10 e 1000
numero = random.randint(10, 1000)

# Calcola la radice quadrata
radice_quadrata = math.sqrt(numero)

# Stampa il risultato arrotondato alla terza cifra decimale
print(f"La radice quadrata di {numero} è {radice_quadrata:.3f}")
