import math
import numpy as np

noms = ["Soleil", "Mercure", "Venus", "Terre", "Mars", "Jupiter", "Saturne", "Uranus", "Neptune"]

CorpsCeleste = np.array([
    [1.989e30, 0.0, 0.0, 0.0, 0.0],
    [3.285e23, 5.791e10, 0.0, 0.0, 4.8e4],
    [4.867e24, 1.082e11, 0.0, 0.0, 3.5e4],
    [5.972e24, 1.496e11, 0.0, 0.0, 2.978e4],
    [6.39e23, 2.279e11, 0.0, 0.0, 2.41e4],
    [1.898e27, 7.785e11, 0.0, 0.0, 1.3e4],
    [5.683e26, 1.433e12, 0.0, 0.0, 9.7e3],
    [8.681e25, 2.877e12, 0.0, 0.0, 6.8e3],
    [1.024e26, 4.503e12, 0.0, 0.0, 5.4e3]
], dtype=float)

#1. Masse de la planète (en kg) | 2. Distance X du Soleil | 3. Distance Y du Soleil | 4. Vitesse X | 5. Vitesse Y | 6. Diamètre de la planète (en km)

CorpsCelesteTest = np.array([
    [1.989e30, 0.0, 0.0, 0.0, 0.0, 13927e2],
    [3.285e23, 69.8e6, 0.0, 0.0, 4.8e4, 48e2],
    [4.867e24, 108.9e6, 0.0, 0.0, 3.5e4, 121e2],
    [5.972e24, 152.1e6, 0.0, 0.0, 2.978e4, 127e2],
    [6.39e23, 249.2e6, 0.0, 0.0, 2.41e4, 67e2],
    [1.898e27, 816.6e6, 0.0, 0.0, 1.3e4, 1398e2],
    [5.683e26, 1514e6, 0.0, 0.0, 9.7e3, 1164e2],
    [8.681e25, 3003e6, 0.0, 0.0, 6.8e3, 507e2],
    [1.024e26, 4545e6, 0.0, 0.0, 5.4e3, 492e2]
], dtype=float)

dt = 3600
iterations = 0
distance_max = 7.375e9 #distance de l'Aphélie de Pluton

PositionX = CorpsCeleste[:, 3]
PositionY = CorpsCeleste[:, 4]


def ForceGravitationnelle(masse_planet, masse_soleil, dx) :
    force = calculerForceGravitationnelle(masse_planet, masse_soleil, dx)
    return force

def calculerForceGravitationnelle(masse_planet, masse_soleil, dx) :
    G = 6.67430e-11
    return G * masse_planet * masse_soleil / dx**2

planets = [
    ("Mercure", 1),
    ("Venus", 2),
    ("Terre", 3),
    ("Mars", 4),
    ("Jupiter", 5),
    ("Saturne", 6),
    ("Uranus", 7),
    ("Neptune", 8)
]

for i in range(iterations):
    print("Iteration", i + 1)
    print("-----------------------------")
    for name, idx in planets:
        m_p = CorpsCeleste[idx][0]
        m_s = CorpsCeleste[0][0]
        dx = float((CorpsCeleste[idx][1]))
        Fx = ForceGravitationnelle(m_p, m_s, dx)
        print("Soleil - " + name + ": Force gravitationnelle X :", Fx)
        ax = Fx / m_p
        CorpsCeleste[idx][3] = CorpsCeleste[idx][3]
        CorpsCeleste[idx][3] += ax * dt  # update vx
        CorpsCeleste[idx][1] += CorpsCeleste[idx][3] * dt  # update x