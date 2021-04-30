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
