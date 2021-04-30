def syracuse(n):
    try:
        n = int(n)
        if n < 1:
            return "Vous n'avez pas saisie une bonne valeur"
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
