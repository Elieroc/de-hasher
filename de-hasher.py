import hashlib

# A modifier
hash = "365d38c60c4e98ca5ca6dbc02d396e53"
wordlist = open('wl.txt', 'r+')

list_passwords_tested = wordlist.readlines()
wordlist.close()

for tested in list_passwords_tested:
    # Enlève le saut de ligne
    tested = tested.rstrip('\n')
    # Va hasher le mot de passe à tester
    hash_tested = hashlib.md5(tested.encode()).hexdigest()
    # Teste si le mot de passe testé hashé correspond au hash
    if (hash_tested != hash) :
        print("Mot de passe testé : ", tested)
        print("Hash : ", hash_tested, "\n")
    else :
        print("\nMot de passe trouvé :", tested)
        break
