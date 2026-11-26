from lecture import lire_config, lire_csv, lire_json
from Ordonnancement.FIFO import ordonancementFIFO
from Ordonnancement.RoundRobin import ordonancementRoundRobin
from ecriture import ecrire_resultats

dossier_inputsT1 = "../Inputs/Test01/"
dossier_outputs = "../Outputs/"

#chemin vers config.txt
config = lire_config(dossier_inputsT1 + "config.txt")

processus = lire_csv(dossier_inputsT1 + config["fichier_processus"])
# =  processus.csv (chemin vers le fichier de processus)

ressources = lire_json(dossier_inputsT1 + config["fichier_ressources"])
# =  ressources.json (chemin vers le fichier de ressources)

energie = lire_csv(dossier_inputsT1 + config["energie"])
# =  energie.csv (chemin vers le fichier d'énergie)

quantum = int(config["quantum"])
# chemin vers le quantum, le texte est converti en entier 

fichier_metriques = dossier_outputs + config["fichier_metriques"]
# = metriques.txt (chemin vers le fichier de métriques)

open(fichier_metriques, "w").close() #clean le fichier si existe, sinon le créer

for algo in config["algorithmes"]:
    historique = []
    #rajouter un strip si pb pour rr

    if algo == "FIFO":
        resultat = ordonancementFIFO(processus, ressources, energie)
        nom_sortie = "FIFO"
    elif algo == "RR":

        #comme rr renvoie termines, historique alloues
        resultat, historique = ordonancementRoundRobin(processus, ressources, energie, quantum)
        nom_sortie = "RoundRobin"

    else:
        print(f"Algorithme non traité")
        continue
    #chemin vers où écrire le résultat (../Outputs/" + "resultats_fifo_global.csv")
    fichier_global = dossier_outputs + config["fichier_global_" + nom_sortie]

    #mm chose
    fichier_allocations = dossier_outputs + config["fichier_allocations_" + nom_sortie]

    
    ecrire_resultats(resultat, ressources, energie, algo, fichier_global, fichier_allocations, fichier_metriques)
