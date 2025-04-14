majuscules = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
minuscules = [chr(i) for i in range(ord('a'), ord('z') + 1)]
chiffres = [str(i) for i in range(10)]

list = majuscules + minuscules + chiffres

message = input("Phrase à chiffrer : ")
decalage = int(input("décalage souhaité"))

def chiffrer(message, decalage):
    result = ''
    for lettre in message:
        if lettre in list:
            index = list.index(lettre)
            index_decale =  (index + decalage)
            result += list[index_decale]
        else:
            result += lettre
    return result

message_code = chiffrer(message, decalage)
print("Message chiffré :", message_code)