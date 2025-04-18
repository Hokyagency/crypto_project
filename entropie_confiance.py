
from entropie import calculer_entropie_mdp_clair

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
        #sys.exit()
    else:
        print("Le mot de passe à été validé avec succés.")

    validation(entropie_total)

    

