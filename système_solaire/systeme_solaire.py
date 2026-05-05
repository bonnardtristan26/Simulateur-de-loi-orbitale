import math
import numpy as np

CorpsCeleste = np.array([["Soleil", 1.989e30, 0.0, 0.0, 0.0, 0.0],
["Mercure", 3.285e23, 5.791e10, 0.0, 0.0, 4.8e4],
["Venus", 4.867e24, 1.082e11, 0.0, 0.0, 3.5e4],
["Terre", 5.972e24, 1.496e11, 0.0, 0.0, 2.978e4]
["Mars", 6.39e23, 2.279e11, 0.0, 0.0, 2.41e4]
["Jupiter", 1.898e27, 7.785e11, 0.0, 0.0, 1.3e4]
["Saturne", 5.683e26, 1.433e12, 0.0, 0.0, 9.7e3]
["Uranus", 8.681e25, 2.877e12, 0.0, 0.0, 6.8e3]
["Neptune", 1.024e26, 4.503e12, 0.0, 0.0, 5.4e3]])

dt = 3600


def ForceGravitationnelle(masse_planet, masse_soleil, dx) :
    force = calculerForceGravitationnelle(masse_planet, masse_soleil, dx)
    return force

def calculerForceGravitationnelle(masse_planet, masse_soleil, dx) :
    G = 6.67430e-11
    return G * masse_planet * masse_soleil / dx


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

def update_positions_and_velocities():
    for name, idx in planets:
        m_p = CorpsCeleste[idx][1]
        m_s = CorpsCeleste[0][1]
        dx = (-CorpsCeleste[idx][2])**2
        Fx = ForceGravitationnelle(m_p, m_s, dx)
        ax = Fx / m_p
        CorpsCeleste[idx][4] += ax * dt  # update vx
        CorpsCeleste[idx][2] += CorpsCeleste[idx][4] * dt  # update x

