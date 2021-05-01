def valid_password(mdp):
    res = 0
    res2 = 0
    res3 = 0
    special_characters = "!@#$%^&*()-+?_=,<>/"

    if len(mdp) >= 8:
        for c in mdp:
            if c in special_characters:
                res += 1
            if c.isdigit():
                res2 += 1
            if c.isalpha():
                res3 += 1
        if res >= 1 and res2 >= 1 and res3 >= 1:
            return True
        else:
            return False
    else:
        return False

# oneliner (un peu long mais découpé en blocs simples), considéré comme lisible en milieu pro
# on utilise des \ pour passer à la ligne (mais que Python recolle tous les morceaux en une seule ligne)
# avantages : lisible, modulable, debuggable, utilise uniquement des fonctions "basiques"
# 
# contrairement à l'implémentation qu'a proposé Sêlêm : je considère que tout caractère autre que chiffre ou lettre est un "caractère spécial"
# pas une bonne idée en pratique (il existe des caractères "non imprimables" qu'on n'a pas envie de retrouver dans sa base de données de mots de passe)

# #def valid_password(mdp):
#    return len(mdp)>7 \
#        and any(map(str.isalpha, mdp)) \
#        and any(map(str.isdigit, mdp))\
#        and any(map(lambda c: not(c.isalnum()),mdp))
