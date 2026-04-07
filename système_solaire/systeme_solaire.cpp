#include <iostream>
#include <vector>
#include <cmath>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

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
// T^2 = (4*pi^2 / G*M) * a^3
double calculerPeriodeOrbitale(double distance, double masseSoleil) {
    const double G = 6.67430e-11;
    return 2 * M_PI * sqrt((distance * distance * distance) / (G * masseSoleil));
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

    // Boucle de simulation
    double dt = 3600 * 24; // Pas de temps en secondes (1 jour)
    int iterations = 365 * 10; // 10 ans
    
    for (int i = 0; i < iterations; ++i) {
        // Mettre à jour chaque planète
        for (size_t j = 1; j < systemeSolaire.size(); ++j) { // Commencer à 1 pour éviter le Soleil
            CorpsCeleste& planete = systemeSolaire[j];
            
            // Calculer la distance au Soleil
            double dx = planete.positionX - soleil.positionX;
            double dy = planete.positionY - soleil.positionY;
            double distance = sqrt(dx * dx + dy * dy);
            
            // Calculer la force gravitationnelle (magnitude)
            double force = calculerForceGravitationnelle(soleil.masse, planete.masse, distance);
            
            // Direction de la force (vers le Soleil)
            double fx = -force * dx / distance;
            double fy = -force * dy / distance;
            
            // Accélération
            double ax = fx / planete.masse;
            double ay = fy / planete.masse;
            
            // Mettre à jour la vitesse
            planete.vitesseX += ax * dt;
            planete.vitesseY += ay * dt;
            
            // Mettre à jour la position
            planete.positionX += planete.vitesseX * dt;
            planete.positionY += planete.vitesseY * dt;
        }
        
        // Afficher la position de la Terre tous les 365 jours
        if (i % 365 == 0) {
            std::cout << "Jour " << i << ": Terre en (" << systemeSolaire[3].positionX / 1.496e11 << ", " << systemeSolaire[3].positionY / 1.496e11 << ") UA" << std::endl;
        }
    }
    
    // Démonstration de la troisième loi de Kepler
    // Les lois de Kepler décrivent le mouvement des planètes :
    // 1ère loi : Les planètes décrivent des orbites elliptiques avec le Soleil en foyer.
    // 2ème loi : Le rayon vecteur balaye des aires égales en des temps égaux.
    // 3ème loi : Le carré de la période est proportionnel au cube du demi-grand axe.
    std::cout << "\nTroisième loi de Kepler: T^2 ∝ a^3" << std::endl;
    std::cout << "Planète\t\tDistance (UA)\tPériode théorique (ans)\tT^2 / a^3" << std::endl;
    
    for (size_t j = 1; j < systemeSolaire.size(); ++j) {
        CorpsCeleste& planete = systemeSolaire[j];
        double distanceUA = planete.positionX / 1.496e11; // Convertir en UA (Terre = 1 UA)
        double periodeAns = calculerPeriodeOrbitale(planete.positionX, soleil.masse) / (365.25 * 24 * 3600); // En années
        double t2_a3 = periodeAns * periodeAns / (distanceUA * distanceUA * distanceUA);
        
        std::cout << planete.nom << "\t\t" << distanceUA << "\t\t" << periodeAns << "\t\t\t" << t2_a3 << std::endl;
    }
    
    return 0;
}