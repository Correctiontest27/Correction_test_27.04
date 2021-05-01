def syracuse(n):
    try:
        n = int(n)
        if n < 1:
            # retourner une chaîne pour indiquer une erreur (sur une fonction en int) : très mauvaise pratique
            #return "Vous n'avez pas saisie une bonne valeur"
            # si on ne veut pas passer par un raise, retourner None est un moyen de montrer qu'on demande un calcul sans résultat
            # on pourrait aussi passer par math.nan pour indiquer des erreurs mathématiques
            return None
        else:
            new_str = []
            while n != 1 :
                if n%2 == 0:
                    n = n//2
                    new_str += [n]
                elif n%2 != 0:
                    n = n*3+1
                    new_str += [n]
        return new_str
    except ValueError as e:
        raise(e)

"""
Version récursive avec "nested function"

def syracuse(n):
    def _tmp(x,lst):
        if x==1:
            return lst + [1]
        elif x%2:
            return _tmp(x*3+1, lst+[x])
        else:
            return _tmp(x//2, lst+[x])
    res=_tmp(n,[])
    # on enlève le premier élément pour respecter la consigne
    return res[1:]
"""