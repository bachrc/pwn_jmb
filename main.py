import codecs
import datetime
import random
import requests

import time


def get_valeurs():
    prenoms = codecs.open("res/prenoms.txt", 'rb', 'utf-8').read().splitlines()
    noms = codecs.open("res/noms.txt", 'rb', 'utf-8').read().splitlines()
    mails = codecs.open("res/mails.txt", 'rb', 'utf-8').read().splitlines()
    entreprises = codecs.open("res/entreprises.txt", 'rb', 'utf-8').read().splitlines()

    return random.choice(prenoms), random.choice(noms), random.choice(mails), random.choice(entreprises)


def inscription(prenom, nom, telephone, mail, entreprise):
    url_params = {
        "_ak": "CzO7LZ0VBeboGx6eDc94Jbs711eSPDru",
        "_as": "5m570J08od",
        "_of": "-7200",
        "_s": "front",
        "limit": "null",
        "max": "null",
        "type": "null"
    }

    headers = {
        "Accept": "application/json, text/plain, */*"
    }

    now = datetime.datetime.now()
    r_ip = requests.get("http://ip.42.pl/raw")

    body = {
        "campaign_id": "150573918210295",
        "app_id": "6",
        "timestamp": now.timestamp(),
        "day": now.day,
        "month": now.month,
        "year": now.year,
        "hour": now.hour,
        "preview": "0",
        "email": mail,
        "firstname": prenom,
        "lastname": nom,
        "phone": telephone,
        "ip": r_ip.text,
        "connector": "mail",
        "customfield_1": entreprise,
        "optin_cgu": 1,
        "optin": 0,
        "optin_partner": 0
    }

    r = requests.post("https://api.socialshaker.com/orm/front/register", params=url_params, headers=headers, data=body)

    if not r.ok:
        print(r.json())
        raise ValueError("Inscription échouée..")

    return r.json()["_id"]


def like(user_id):
    url_params = {
        "_ak": "CzO7LZ0VBeboGx6eDc94Jbs711eSPDru",
        "_as": "5m570J08od",
        "_s": "front",
        "campaignId": "150573918210295",
        "appId": "6",
        "type": "photo"
    }

    headers = {
        "Accept": "application/json, text/plain, */*"
    }

    now = datetime.datetime.now()
    r_ip = requests.get("http://ip.42.pl/raw")

    body = {
        "_s": "front",
        "_ak": "CzO7LZ0VBeboGx6eDc94Jbs711eSPDru",
        "timestamp": now.timestamp(),
        "day": now.day,
        "month": now.month,
        "year": now.year,
        "hour": now.hour,
        "preview": "0",
        "email": mail,
        "firstname": prenom,
        "lastname": nom,
        "phone": telephone,
        "ip": r_ip.text,
        "connector": "mail",
        "customfield_1": entreprise,
        "optin_cgu": 1,
        "optin": 0,
        "optin_partner": 0
    }


if __name__ == "__main__":
    prenom_defaut, nom_defaut, domaine_defaut, entreprise_defaut = get_valeurs()

    prenom = input("Entrez votre faux prénom [%s] : " % prenom_defaut)
    prenom = prenom or prenom_defaut

    nom = input("Entrez votre faux nom [%s] : " % nom_defaut)
    nom = nom or nom_defaut

    telephone_defaut = "0" + str(random.choice([6, 7])) + "".join([str(random.randint(0, 9)) for _ in range(8)])
    telephone = input("Entrez votre faux téléphone [%s] : " % telephone_defaut)
    telephone = telephone or telephone_defaut

    mail_defaut = prenom[0] + nom + "@" + domaine_defaut
    mail = input("Entrez votre faux mail (pas de verif.) [%s] : " % mail_defaut)
    mail = mail or mail_defaut

    entreprise = input("Entrez votre fausse entreprise (pas de verif.) [%s] : " % entreprise_defaut)
    entreprise = entreprise or entreprise_defaut

    print("Ces valeurs vont être envoyées : \nNom : %s %s\nTéléphone : %s\nMail : %s\nEntreprise : %s" %
          (prenom, nom, telephone, mail, entreprise))

    """
    try:
        user_id = inscription(prenom, nom, telephone, mail, entreprise)
        print("Inscription effectuée avec succès !")
    """

