#ifndef SYSTEME_SOLAIRE_H
#define SYSTEME_SOLAIRE_H

#include <vector>
#include <string>

// Structure pour représenter une planète
struct Planete {
    std::string nom;
    double masse;  // en kg
    double rayon;  // en km
    double distanceSoleil;  // en UA (unités astronomiques)
    double vitesseOrbitale;  // en km/s
};

// Classe pour simuler le système solaire
class SystemeSolaire {
private:
    std::vector<Planete> planetes;

public:
    SystemeSolaire();
    void ajouterPlanete(const Planete& planete);
    void simulerOrbite(double temps);
    void afficherSysteme() const;
    void caclulerForceGravitationnelle(double distance) const;
    void calculerVitesseOrbitale(double distance) const;
};

#endif // SYSTEME_SOLAIRE_H