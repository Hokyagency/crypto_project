import math

mot_de_passe = input("Entrez votre mot de passe : ")

def calculer_entropie_mdp_clair(mot_de_passe):

    longueur = len(mot_de_passe)
    if longueur == 0:
        return 0

    alphabet_base = ""
    majuscules = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    minuscules = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    chiffres = [str(i) for i in range(10)]
    symboles = symboles = "!@#$%^&*()_+=-`~[]{};':\",./<>?"    

    contient_majuscule = False
    contient_chiffre = False
    contient_symbole = False

    for char in mot_de_passe:
        if char in majuscules:
            contient_majuscule = True
        elif char in chiffres:
            contient_chiffre = True
        elif char in symboles:
            contient_symbole = True

    alphabet_base = minuscules
    if contient_majuscule:
        alphabet_base += majuscules
    if contient_chiffre:
        alphabet_base += chiffres
    if contient_symbole:
        alphabet_base += symboles

    taille_alphabet = len(set(alphabet_base))

    if taille_alphabet == 0:
        return 0 

    entropie_par_caractere = math.log2(taille_alphabet)
    entropie_totale = longueur * entropie_par_caractere
    return entropie_totale

entropie = calculer_entropie_mdp_clair(mot_de_passe)
print(f"L'entropie de '{mot_de_passe}' est : {entropie:.2f} bits")
