# py -m unittest


# isalnum: prend une chaîne en argument et vérifie si elle
# est alphanumérique

# Best practice
def isalnum(mot):
    for l in mot:
        if not (48 <= ord(l) <= 57 or 65 <= ord(l) <= 90 or 97 <= ord(l) <= 122):
            return False
    return True


# Baby practice :
# def isalnum(mot):
#     for l in mot:
#         if 48 <= ord(l) <= 57:
#             pass
#             # print(f"{l} est un chiffre")
#         elif 65 <= ord(l) <= 90 or 97 <= ord(l) <= 122:
#             pass
#             # print(f"{l} est une lettre")
#         else:
#             return False
#     return True


# print(isalnum("32coucou"))
# print(isalnum("CouCo46819u"))
# print(isalnum("061498765432"))
# print(isalnum("061498765_(/!,)"))


# tolower : convertis une chaîne en minuscules

# Best practice :
def tolower(mot):
    result = ""
    for l in mot:
        if 65 <= ord(l) <= 90:
            # print(f"{l} est une majuscule")
            lettre_valeur = ord(l)+32
            result += chr(lettre_valeur)
        else:
            result += l
    return result


# lencmp : compare la longueur de 2 chaines de caractère
def lencmp(text1, text2):
    text1 = len(text1)
    text2 = len(text2)
    if text1 > text2:
        return 1
    elif text1 < text2:
        return -1
    else:
        return 0


# strcmp : compare l'ordre alphabétique de 2 chaines de caratère
    # si la 1er lettre est identique : compare la longueur de la chaine
    #  pas de différence entre A et a (ex: A = a)
def strcmp(text1, text2):
    text1 = tolower(text1)
    text2 = tolower(text2)
    for c in text1:
        for d in text2:
            if c == d:
                return lencmp(text1, text2)
            elif ord(c) > ord(d):
                return 1
            elif ord(c) < ord(d):
                return -1
