from entropie import *
from entropie_confiance import *

def redondance(entropie_total, longueur, L=8):

    entropie_par_caractere = entropie_total / longueur
    redondance = L - entropie_par_caractere
    taux_redondance = 1 - (entropie_par_caractere / L)
    print(f"Redondance (en bits) : {redondance:.4f}")
    print(f"Taux de redondance : {taux_redondance * 100:.2f} %")
    return redondance, taux_redondance

#dans le try
#longueur_mdp = len(confirmed_password)
#r, taux = redondance(entropie_mdp, longueur_mdp)