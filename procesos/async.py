import asyncio
import random

async def mensaje(txt, wait = 1):
    print(txt)
    await asyncio.sleep(wait)

async def ronda(jugador1, jugador2):
    txt = f"{jugador1} vs {jugador2}: "
    resultados = [i for i in range(0, 3)]
    cambio = ['Piedra', 'Papel', 'Tijeras']
    eleccionJ1 = random.choice(resultados)
    eleccionJ2 = random.choice(resultados)

    while eleccionJ1 == eleccionJ2:
        await mensaje(txt + f"Empate con {cambio[eleccionJ1]}")
        eleccionJ1 = random.choice(resultados)
        eleccionJ2 = random.choice(resultados)

    if resultados[eleccionJ1 - 1] == eleccionJ2:
        await mensaje(txt + f"Gana {jugador1} con {cambio[eleccionJ1]}, pierde {jugador2} con {cambio[eleccionJ2]}")
        return jugador1
    else:
        await mensaje(txt + f"Gana {jugador2} con {cambio[eleccionJ2]}, pierde {jugador1} con {cambio[eleccionJ1]}")
        return jugador2


async def main():
    # Schedule three calls *concurrently*:
    await mensaje("Vamos a presenciar un torneo ficticio de piedra, papel o tijeras en...", 3)
    for i in range(3, 0, -1):
        await mensaje(i, 0.5)
    print("\n¡Que comienze el torneo!\n")
    
    L = await asyncio.gather(
        ronda('Mike', 'Carl'),
        ronda('John', 'Mary'),
        ronda('Carla', 'Kiwi'),
        ronda('Tim', 'Jake')
    )
    
    await mensaje("\nLos finalistas de esta ronda son:", 4)
    for i in range(len(L)):
        if i == len(L) - 1:
            print("y finalmente...", end=" ")
        await mensaje(L[i])
    await mensaje("\nComenzando la siguiente ronda...\n", 3)
    L = await asyncio.gather(
        ronda(L[0], L[1]),
        ronda(L[2], L[3])
        )
    
    await mensaje("\n ¡Y ahora las finales!", 3)
    await mensaje(f"Será {L[0]} contra {L[1]} \n")

    ganador = await ronda(L[0], L[1])

    print(f"\n¡¡¡EL GANADOR DEFINITIVO DE PIEDRA PAPEL O TIJERAS ES {ganador}!!!")
            
asyncio.run(main())