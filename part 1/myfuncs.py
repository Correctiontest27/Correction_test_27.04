# py -m unittest


# isalnum: prend une chaîne en argument et vérifie si elle
# est alphanumérique

# Best practice
def isalnum(mot):
    for l in mot :
        if not (48<=ord(l)<=57 or 65<=ord(l)<=90 or 97<=ord(l)<=122):
            return False
   return True


# Baby practice :
#def isalnum(mot):
    #for l in mot :
        # if 48<=ord(l)<=57 :
        #     pass
        #     # print(f"{l} est un chiffre")
        # elif 65<=ord(l)<=90 or 97<=ord(l)<=122:
        #     pass
        #     # print(f"{l} est une lettre")
        # else :
        #     return False
#return True


#tolower : convertis une chaîne en minuscules

# Best practice : 
def tolower(mot):
    result = ""
    for l in mot :
        if 65<=ord(l)<=90:
            # print(f"{l} est une majuscule")
            lettre_valeur = ord(l)+32
            result += chr(lettre_valeur)
        else : 
            result += l
    return result
