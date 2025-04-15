al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
message = input("Entrez votre phrase : ")
decalage = int(input("Entrez le décalage : "))

def cesar(message, decalage):
    resultat = ""
    for lettre in message:
        if lettre in al:
            index = al.index(lettre)
            index_decale = (index + decalage) % 26
            resultat += al[index_decale]
        else:
            resultat += lettre
    return resultat

message_code = cesar(message, decalage)
print("Message chiffré :", message_code)


def dechiffrer(message, decalage):
    resultat = ""
    for lettre in message:
        if lettre in al:
            index = al.index(lettre)
            index_decale = (index - decalage) % 26
            resultat -= al[index_decale]
        else:
            resultat -= lettre
    return resultat

message_decode = dechiffrer(message, decalage)
print("Message déchiffré :", message_decode)