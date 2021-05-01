import hashlib

def sha256(string):
    h=hashlib.sha256()
    h.update(str.encode(string))
    return h.hexdigest()

def blake(string):
    h = hashlib.blake2b()
    h.update(str.encode(string))
    return h.hexdigest()


def check_password(pwd, hash, method):
    if method == "blake":
        if blake(pwd) == hash:
            return True
        return False
    elif method == "sha256":
        if sha256(pwd) == hash:
            return True
        return False
    else:
        print("your 'method' argument is not valid")

# print(sha256("adrian"))
# print(sha256(sha256(sha256("adrian"))))
# print(sha256(sha256("adrian")))
print(sha256("stephanie"))
