import math
import numpy as np

CorpsCeleste = np.array([["Soleil", 1.989e30, 0.0, 0.0, 0.0, 0.0],
["Mercure", 3.285e23, 5.791e10, 0.0, 0.0, 4.8e4],
["Venus", 4.867e24, 1.082e11, 0.0, 0.0, 3.5e4],
["Terre", 5.972e24, 1.496e11, 0.0, 0.0, 2.978e4],
["Mars", 6.39e23, 2.279e11, 0.0, 0.0, 2.41e4],
["Jupiter", 1.898e27, 7.785e11, 0.0, 0.0, 1.3e4],
["Saturne", 5.683e26, 1.433e12, 0.0, 0.0, 9.7e3],
["Uranus", 8.681e25, 2.877e12, 0.0, 0.0, 6.8e3],
["Neptune", 1.024e26, 4.503e12, 0.0, 0.0, 5.4e3]])

dt = 3600
iterations = 1000

def ForceGravitationnelle(masse1, masse2, distance) :
    force = calculerForceGravitationnelle(masse1, masse2, distance)
    print("Force gravitationnelle :", force)

def calculerForceGravitationnelle(masse1, masse2, distance) :
    G = 6.67430e-11
    return G * masse1 * masse2 / (distance * distance)

for i in range(iterations):
    print("Iteration", i + 1)
    print("-----------------------------")
    print("Soleil - Mercure: ", ForceGravitationnelle(CorpsCeleste[0][1], CorpsCeleste[1][2], CorpsCeleste[1][5]))
    print("Soleil - Venus: ", ForceGravitationnelle(CorpsCeleste[0][1], CorpsCeleste[2][2], CorpsCeleste[2][5]))
    print("Soleil - Terre:", ForceGravitationnelle(CorpsCeleste[0][1], CorpsCeleste[3][2], CorpsCeleste[3][5]))
    print("Soleil - Mars:", ForceGravitationnelle(CorpsCeleste[0][1], CorpsCeleste[4][2], CorpsCeleste[4][5]))
    print("Soleil - Jupiter", ForceGravitationnelle(CorpsCeleste[0][1], CorpsCeleste[5][2], CorpsCeleste[5][5]))
    print("Soleil - Saturne",ForceGravitationnelle(CorpsCeleste[0][1], CorpsCeleste[6][2], CorpsCeleste[6][5]))
    print("Soleil - Uranus", ForceGravitationnelle(CorpsCeleste[0][1], CorpsCeleste[7][2], CorpsCeleste[7][5]))
    print("Soleil - Neptune", ForceGravitationnelle(CorpsCeleste[0][1], CorpsCeleste[8][2], CorpsCeleste[8][5]))
    print("-----------------------------")

