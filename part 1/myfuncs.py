# py -m unittest
def isalnum(mot):
#Trouver comment retourner juste chiffres et lettres :
    for l in mot :
        if 48<=ord(l)<=57 :
            pass
            # print(f"{l} est un chiffre")
        elif 65<=ord(l)<=90 or 97<=ord(l)<=122:
            pass
            # print(f"{l} est une lettre")
        else :
            return False

    return True

# print(isalnum("32coucou"))
# print(isalnum("CouCo46819u"))
# print(isalnum("061498765432"))
# print(isalnum("061498765_(/!,)"))





def tolower(mot):
# """
#     tolower : convertis une chaîne en minuscules
#     Prend une chaîne en paramètre et retourne la même chaîne avec toutes les lettres majuscules converties en
#     minuscules (sans changer le reste)
#     Exemple : tolower("AbCd1234#") => "abcd1234#"
# """


    result = ""
    for l in mot :
        if 65<=ord(l)<=90:
            # print(f"{l} est une majuscule")
            lettre_valeur = ord(l)+32
            result += chr(lettre_valeur)
        else : 
            result += l
    return(result)


# print(tolower("EMILIE2000"))
# print(tolower("YouPiLaVie"))
# print(tolower("teST2...laMueRte!"))