# Conversion lettres -> nombres
def text_a_nombres(text):
    text = text.upper().replace(' ', '')    #pour mettre en majuscule + enlever les espaces
    return [ord(c) - ord('A') for c in text]    #calcule la position de la lettre dans l'alphabet

# Conversion nombres -> lettres
def conversion_nombres_text(nombres):
    return ''.join(chr(n % 26 + ord('A')) for n in nombres) #donne le code ASCII du caractère 'A', qui est 65

# réalise une multiplication entre une matrice et un vecteur
def matrice_vecteur_mult(matrice, vecteur): 
    result = []
    for row in matrice:
        val = sum(row[i] * vecteur[i] for i in range(len(vecteur)))
        result.append(val % 26)
    return result

# Chiffrement
def encrypt(text, key_matrice):
    nombres = text_a_nombres(text)
    n = len(key_matrice)    #détermine la taille de la clés
    
    # Padding si besoin
    if len(nombres) % n != 0:
        nombres += [0] * (n - len(nombres) % n)
    
    ciphertext = []
    for i in range(0, len(nombres), n):
        block = nombres[i:i+n]  #n représente la taille de la clé, i:i+n cela permet de diviser la liste en blocs de n valeurs
        encrypted_block = matrice_vecteur_mult(key_matrice, block)  #qui effectue la multiplication entre la matrice key_matrice et le bloc block, transforme texte en nombres
        ciphertext.extend(encrypted_block)  #ajoute les valeurs du bloc chiffré
    
    return conversion_nombres_text(ciphertext)  #retourne texte chiffré en texte

# Exemple d'utilisation
key = [
    [3, 3],
    [2, 5]
]

def entrez_text():
    return input("entrez votre phrase à chiffrer : ")

ciphertext = encrypt(entrez_text(), key)

print(f"Texte chiffré : {ciphertext}")