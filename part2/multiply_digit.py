def multiply_digit(numb):
    x = ''
    y = 1
    if numb != 0:
        mark = True
        if numb < 0:
            numb = numb * -1
            mark = False
        t = str(numb)
        for i in t:
            if i != '0':
                x += i
        for i in x:
            i = int(i)
            y *= i
        y = str(y)
        if mark:
            return y
        else:
            return '-'+y
    else:
        return '0'

_MODE_ALTERNATIF=False

# version recursive
def multiply_digit_int(n):
    """
    Fonction intermédiaire qui prend un int en entrée, retourne un int
    La "vraie" fonction va l'appeler et convertir le résultat
    """
    if n<0:
        # devinez ce qu'on fait là?
        return -multiply_digit_int(-n)
    elif n<=9:
        return n
    else:
        # astuce de calcul ici, devinez ce qui se passe?
        # considéré comme "évident" pour programmeur expérimenté, mais pas forécement pour des junior
        # c'est courant en Python, si vous arrivez à le trouver avec google expliquez aux collègues les mots clés recherchés
        return multiply_digit_int(n//10)*(n%10 or 1)


def multiply_digit_rec(n):
    """
    Version récursive
    Pour gerer les chaines vides on decide qu'on retourne '0' (pas dans l'énoncé).
    Pareil si on nous donne '0' en entrée.
    """
    if n=='':
        return '0'
    # volontairement je ne renvoie pas de ValueError parce que int() le fera pour moi si besoin
    return str(multiply_digit_int(int(n)))

# devinez aussi à quoi sert cette ligne
if(_MODE_ALTERNATIF):
    multiply_digit = multiply_digit_rec