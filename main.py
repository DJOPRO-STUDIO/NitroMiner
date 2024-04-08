import random
import string
import requests
import re




counter = 0
counter_success = 0


def verifier_lien_cadeau_nitro(lien_cadeau):
    try:
        response = requests.get(lien_cadeau)
        if response.status_code == 200 and 'redeem' in response.url:
            return True, "Valide"
        else:
            return False, "Invalide"
    except Exception as e:
        return False, f"Erreur: {str(e)}"
    
def generer_chaine():
    caracteres = string.ascii_letters + string.digits
    chaine = ''.join(random.choices(caracteres, k=16))
    return chaine



while True:
    ran = generer_chaine()
    link = f"https://discord.gift/{ran}"

    counter = counter + 1

    valide, message = verifier_lien_cadeau_nitro(link)
    print(f"Le lien cadeau Nitro {link} est {message}")
    # SHOWER APP WEB
    
    
    if valide:
        counter_success = counter_success + 1
        f = open("nitro_links.txt", "a")
        f.write(link)
        f.close()

