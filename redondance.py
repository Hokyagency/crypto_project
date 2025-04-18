from entropie_confiance import *
from entropie import *

def redondance(entropie_total, longueur, L=8):

    entropie_par_caractere = entropie_total / longueur
    redondance = L - entropie_par_caractere
    taux_redondance = 1 - (entropie_par_caractere / L)
    print(f"Redondance (en bits) : {redondance:.4f}")
    print(f"Taux de redondance : {taux_redondance * 100:.2f} %")
    return redondance, taux_redondance


entropie = calculer_entropie_mdp_clair(mot_de_passe)
print(f"L'entropie de '{mot_de_passe}' est : {entropie:.2f} bits")
confiance(entropie)
validation(entropie)

longueur_mdp = len(mot_de_passe)
redondance(entropie, longueur_mdp)


#mettre dans le try les deux lignes ci-dessous
#longueur_mdp = len(confirmed_password)
#r, taux = redondance(entropie_mdp, longueur_mdp)