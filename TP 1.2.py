import random
import math
import matplotlib.pyplot as plt
import statistics as stats
import collections

numeros_ruleta = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                  26, 27, 28, 29, 30, 31, 32, 33, 35, 35, 36]


# MENU
def menu():
    print("Bienvenidos a la Ruleta")
    print("Menu:")
    print("1 - Martingala")
    # continua menu

    rta = int(input("Ingrese la opcion elegida: "))
    return rta


def martingala():
    # MARTINGALA
    dinero = []
    rta = int(input("Ingrese 1 si quiere apostar a impar o 2 si quiere apostar a par: "))
    monto = int(input("Ingrese apuesta inicial: "))
    t = 0
    dinero.append(0)
    dinero.append(monto)  # monto inicial
    ganado = False
    # impar
    if rta == 1:
        while ganado == False:
            t = t + 1
            n = random.randint(1, 36)
            if n % 2 == 0 :
                x = len(dinero)
                dinero.append(dinero[x - 1] * 2 + 2)
            else:
                ganado = True
                print("Gano en tirada: ", t)
                print(dinero)
                x = len(dinero)
                x1 = range(0, x)
                plt.plot(x1, dinero)
                plt.show()


rta = menu()
if rta == 1:
    martingala()
