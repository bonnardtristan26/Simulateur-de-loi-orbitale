#include <iostream>
#include <vector>
#include <cmath>

// Structure pour représenter un corps céleste
struct CorpsCeleste {
    std::string nom;
    double masse;
    double positionX, positionY;
    double vitesseX, vitesseY;
};

// Fonction pour calculer la force gravitationnelle
double calculerForceGravitationnelle(double masse1, double masse2, double distance) {
    const double G = 6.67430e-11; // Constante gravitationnelle
    return G * masse1 * masse2 / (distance * distance);
}

// Fonction pour calculer la période orbitale selon la troisième loi de Kepler
double calculerPeriodeOrbitale(double distance, double masseSoleil) {
    const double G = 6.67430e-11;
    return 2 * M_PI * sqrt((distance * distance * distance) / (G * masseSoleil));
}

void caclulerForceGravitationnelle(double masse1, double masse2, double distance) {
    double force = calculerForceGravitationnelle(masse1, masse2, distance);
    std::cout << "Force gravitationnelle: " << force << " N" << std::endl;
}

void calculerVitesseOrbitale(double distance, double masseSoleil) {
    const double G = 6.67430e-11;
    double vitesse = sqrt(G * masseSoleil / distance);
    std::cout << "Vitesse orbitale: " << vitesse << " m/s" << std::endl;
}


int main() {
    // Initialisation des corps célestes (exemple simple avec Soleil et Terre)
    std::vector<CorpsCeleste> systemeSolaire;
    
    CorpsCeleste soleil = {"Soleil", 1.989e30, 0.0, 0.0, 0.0, 0.0};
    CorpsCeleste mercure = {"Mercure", 3.285e23, 5.791e10, 0.0, 0.0, 4.8e4};
    CorpsCeleste venus = {"Venus", 4.867e24, 1.082e11, 0.0, 0.0, 3.5e4};
    CorpsCeleste terre = {"Terre", 5.972e24, 1.496e11, 0.0, 0.0, 2.978e4};
    CorpsCeleste mars = {"Mars", 6.39e23, 2.279e11, 0.0, 0.0, 2.41e4};
    CorpsCeleste jupiter = {"Jupiter", 1.898e27, 7.785e11, 0.0, 0.0, 1.3e4};
    CorpsCeleste saturne = {"Saturne", 5.683e26, 1.433e12, 0.0, 0.0, 9.7e3};
    CorpsCeleste uranus = {"Uranus", 8.681e25, 2.877e12, 0.0, 0.0, 6.8e3};
    CorpsCeleste neptune = {"Neptune", 1.024e26, 4.503e12, 0.0, 0.0, 5.4e3};
    
    systemeSolaire.push_back(soleil);
    systemeSolaire.push_back(mercure);
    systemeSolaire.push_back(venus);
    systemeSolaire.push_back(terre);
    systemeSolaire.push_back(mars);
    systemeSolaire.push_back(jupiter);
    systemeSolaire.push_back(saturne);
    systemeSolaire.push_back(uranus);
    systemeSolaire.push_back(neptune);

    // Boucle de simulation (à compléter)
    double dt = 3600; // Pas de temps en secondes (1 heure)
    int iterations = 1000;
    
    for (int i = 0; i < iterations; ++i) {
        caclulerForceGravitationnelle(soleil.masse, mercure.masse, 5.791e10);
        calculerForceGravitationnelle(soleil.masse, venus.masse, 1.082e11);
        calculerForceGravitationnelle(soleil.masse, terre.masse, 1.496e11);    
        calculerForceGravitationnelle(soleil.masse, mars.masse, 2.279e11);
        calculerForceGravitationnelle(soleil.masse, jupiter.masse, 7.785e11);
        calculerForceGravitationnelle(soleil.masse, saturne.masse, 1.433e12);
        calculerForceGravitationnelle(soleil.masse, uranus.masse, 2.877e12);
        calculerForceGravitationnelle(soleil.masse, neptune.masse, 4.503e12);

        claculerPeriodeOrbitale(5.791e10, soleil.masse);
        calculerPeriodeOrbitale(1.082e11, soleil.masse);
        calculerPeriodeOrbitale(1.496e11, soleil.masse);
        calculerPeriodeOrbitale(2.279e11, soleil.masse);
        calculerPeriodeOrbitale(7.785e11, soleil.masse);
        calculerPeriodeOrbitale(1.433e12, soleil.masse);
        calculerPeriodeOrbitale(2.877e12, soleil.masse);
        calculerPeriodeOrbitale(4.503e12, soleil.masse);

    }
    
    return 0;
}