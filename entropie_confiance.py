import math
import sys

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

def confiance(entropie_total):
    if entropie_total < 15:
        print("Votre mot de passe à un niveau de sécurité de 1/10")
    elif 15 < entropie_total < 30:
        print("Votre mot de passe à un niveau de sécurité de 2/10")
    elif 30 < entropie_total < 40:
        print("Votre mot de passe à un niveau de sécurité de 3/10")
    elif 40 < entropie_total < 50:
        print("Votre mot de passe à un niveau de sécurité de 4/10")
    elif 50 < entropie_total < 60:
        print("Votre mot de passe à un niveau de sécurité de 5/10")
    elif 60 < entropie_total < 70:
        print("Votre mot de passe à un niveau de sécurité de 6/10")
    elif 70 < entropie_total < 80:
        print("Votre mot de passe à un niveau de sécurité de 7/10")
    elif 80 < entropie_total < 90:
        print("Votre mot de passe à un niveau de sécurité de 8/10")
    elif 90 < entropie_total < 100:
        print("Votre mot de passe à un niveau de sécurité de 9/10")
    else:
        print("Votre mot de passe à un niveau de sécurité de 10/10")

def validation(entropie_total):
    if entropie_total < 65:
        print("Votre mot de passe est trop faible, changez le.")
        sys.exit()
    else:
        print("Le mot de passe à été validé avec succés.")

entropie = calculer_entropie_mdp_clair(mot_de_passe)
print(f"L'entropie de '{mot_de_passe}' est : {entropie:.2f} bits")
confiance(entropie)
validation(entropie)

