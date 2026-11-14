#Lecture des fichiers (diff méthodes par fic)
def lire_json(fichier):
    """
    Lit un fichier JSON et retourne son contenu sous forme de dictionnaire.
    
    :param fichier: Chemin vers le fichier JSON à lire.
    :return: Dictionnaire représentant le contenu du fichier JSON.
    """
    import json
    with open(fichier, mode='r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def lire_config(fichier):
    """
    Lit le fichier de configuration et retourne un dictionnaire contenant les paramètres.
    
    :return: Dictionnaire contenant les paramètres de configuration.
    """
    liste_elms = []
    with open(fichier, mode="r", encoding="utf-8") as f:

       for elm in f :
           if elm.startswith("#") or elm.startswith("\n"): 
                continue # On ignore les lignes de commentaires
           elm = elm.strip()
           elm = elm.split("=")
           liste_elms.append(elm)

    
    dico = {}
    for i in range(len(liste_elms)):
       for j in range(len(liste_elms[i])):
            liste_elms[i][j] = liste_elms[i][j].strip() 
            #print(liste_elms[i][j]) 

       cle = liste_elms[i][0]
       valeur = liste_elms[i][1]
       if cle == "algorithmes":
            valeur = valeur.split(",")
       dico[cle] = valeur

    return dico


def lire_csv(fichier):
    """
    Lit un fichier CSV et retourne une liste de dictionnaires représentant les lignes du fichier.
    
    :param fichier: Chemin vers le fichier CSV à lire.
    :return: Liste de dictionnaires où chaque dictionnaire représente une ligne du fichier CSV.
    """
    liste_dictionnaires = []
    

    with open(fichier, mode='r', encoding='utf-8') as f:
        ligne = f.readline()

        ligne = ligne.strip() # Enlève les espaces en début et fin de ligne

        liste_entetes = ligne.split(",") # Mets dans une liste les entêtes en séparant dès qu'il ya une virgule

        for elm in f: # Pour les lignes suivantes du fichier 
            elm = elm.strip() # Enlève les espaces en début et fin de ligne
            if elm == "": # Si la ligne est vide on passe à la suivante
                continue 
            liste_valeurs = elm.split(",") # Met dans une liste les valeurs de la ligne en séparant dès qu'il ya une virgule

            dico = {} # Notre dictionnaire pour mettre dans la liste

            for i in range(len(liste_entetes)):
                val = liste_valeurs[i]
                if val.isdigit():
                    val = int(val)
                dico[liste_entetes[i]] = val
            liste_dictionnaires.append(dico)

    return liste_dictionnaires


def lire_ligne(fichier, indice):
    """
    Renvoie le dictionnaire de la ligne n° 'indice' d'un fichier CSV (0 = première ligne de données).
    Ex : lire_ligne(".../processus.csv", 0) -> {'id_processus': 'P1', 'date_soumission': '0', ...}
    """
    lignes = lire_csv(fichier)
    return lignes[indice]


# #Exemple d'utilisation
# print(lire_ligne("../Inputs/Test01/processus.csv", 0)) #lit toute la ligne de p1 (0)

# # {'id_processus': 'P1', 'date_soumission': '0', 'duree_execution': '5', 'ram_necessaire': '512', 'priorite': '10', 'date_butoir': '20'}

# p2 = lire_ligne("../Inputs/Test01/processus.csv", 1) # P2
# print(p2["date_butoir"]) #15   

# print("energie test")
# print(lire_ligne("../Inputs/Test01/energie.csv", 17)) #instant

# e1 = lire_ligne("../Inputs/Test01/energie.csv", 17) 
# print(e1["instant"]) 

print(lire_config("../Inputs/Test01/config.txt"))
 #fifo,...

print(lire_json("../Inputs/Test01/ressources.json"))