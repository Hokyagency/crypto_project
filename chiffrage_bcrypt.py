import bcrypt

def chiffrage_bcrypt(mot_de_passe):
    salt = bcrypt.gensalt()
    mdp_bytes = mot_de_passe.encode('utf-8')
    mdp_hache = bcrypt.hashpw(mdp_bytes, salt)

    return mdp_hache