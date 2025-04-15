import random

password = input("Entrez votre mot de passe : ")
cle = input("Entrez la clé de chiffrement : ")

def chiffrer_vigenere(password, cle):
    majuscules = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    minuscules = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    chiffres = [str(i) for i in range(10)]
    liste = majuscules + minuscules + chiffres

    result = ''
    cle_complete = ''

    # Étendre la clé à la taille du mot de passe
    while len(cle_complete) < len(password):
        cle_complete += cle
    cle_complete = cle_complete[:len(password)]

    print("Clé utilisée :", cle_complete)

    for i in range(len(password)):
        lettre = password[i]
        lettre_cle = cle_complete[i]

        if lettre in liste and lettre_cle in liste:
            index_lettre = liste.index(lettre)
            index_cle = liste.index(lettre_cle)
            index_decale = (index_lettre + index_cle) % len(liste)
            result += liste[index_decale]
        else:
            result += lettre  # Ne pas chiffrer les caractères spéciaux

    return result

message_code = chiffrer_vigenere(password, cle)
print("Message chiffré :", message_code)
