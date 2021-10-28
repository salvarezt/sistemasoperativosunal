f = open('texto.txt', 'w')

def construirTablero():
    tablero = """
        - T* - C* - A* - D* - R* - A* - C* - T* -\n
        - P* - P* - P* - P* - P* - P* - P* - P* -\n
        -    -    -    -    -    -    -    -    -\n
        -    -    -    -    -    -    -    -    -\n
        -    -    -    -    -    -    -    -    -\n
        -    -    -    -    -    -    -    -    -\n
        - P+ - P+ - P+ - P+ - P+ - P+ - P+ - P+ -\n
        - T+ - C+ - A+ - D+ - R+ - A+ - C+ - T+ -\n
        """
    return tablero

f.write("Así es como se ve un tablero de ajedrez:\n")
f.write(construirTablero())
f.write("En este caso, las fichas están distribuidas como:\n")
f.write("T: Torre - C: Caballo - A: Alfil - D: Dama - R: Rey\n")
f.write("Los que tienen un asterisco son las fichas negras, las otras son las fichas blancas. ")
f.write("¿Puedes modificarlo?")

f.close()

