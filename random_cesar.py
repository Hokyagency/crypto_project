import random

majuscules = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
minuscules = [chr(i) for i in range(ord('a'), ord('z') + 1)]
chiffres = [str(i) for i in range(10)]

list = majuscules + minuscules + chiffres

message = input("Phrase à chiffrer : ")


def chiffrer(message):
    result = ''
    n = len(list)
    decalage = random.randint(1,n+1)
    for lettre in message:
        if lettre in list:
            index = list.index(lettre)
            index_decale =  (index + decalage) % n
            result += list[index_decale]   
        else:
            result += lettre
    print("Décalage :", decalage) 
    return result 


message_code = chiffrer(message)
print("Message chiffré :", message_code)
