
import csv
import os


def verifier_contraintes(processus, ressources, energie):
    """
    Vérifie que les allocations respectent les contraintes de RAM et d'énergie
    Retourne une liste d'erreurs
    """

    erreurs = []
    date_max = max((p["date_fin"] for p in processus), default=0)

    for t in range(date_max):

        actifs = [
            p for p in processus
            if p["date_debut"] <= t < p["date_fin"]
        ]

        ram = sum(p["ram_necessaire"] for p in actifs)
        nb_cpu = len(actifs)

        # Vérifier la RAM
        if ram > ressources["ramTotale"]:
            erreurs.append(f"RAM dépassée à t={t} : {ram}")

        # Vérifier l'énergie
        energie_t = next(
            (e["energie_disponible"] for e in energie if e["instant"] == t),
            0
        )

        cpu_max = min(
            ressources["nbProcesseurs"],
            energie_t // ressources["energieParProc"]
        )

        if nb_cpu > cpu_max:
            erreurs.append(f"Énergie insuffisante à t={t}")

    return erreurs


def ecrire_csv(processus, fichier, colonnes):
    """
    Permet d'enregistrer une liste de processus dans un fichier csv
    """

    os.makedirs(os.path.dirname(fichier) or ".", exist_ok=True)

    with open(fichier, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=colonnes)
        writer.writeheader()

        for p in processus:
            writer.writerow({c: p[c] for c in colonnes})

def calculer_metriques(processus, ressources, energie, allocations=None):
    """
    Calcul des métriques
    Retourne les métriques à mettre dans le csv pour un processus
    """

    energie_disponible = sum(e["energie_disponible"] for e in energie)

    if not processus:
        return {
            "temps_attente_moyen": 0,
            "temps_reponse_moyen": 0,
            "makespan": 0,
            "energie_consomme_totale": 0,
            "energie_disponible_totale": energie_disponible,
            "taux_utilisation": 0
        }

    if allocations is None:
        allocations = processus

    n = len(processus)

    attente = sum(p["date_fin"] - p["date_soumission"] - p["duree_execution"] for p in processus) / n

    reponse = sum(p["date_debut"] - p["date_soumission"] for p in processus) / n

    makespan = max(p["date_fin"] for p in processus)

    energie_consommee = sum(sum(1 for a in allocations if a["date_debut"] <= t < a["date_fin"]) * ressources["energieParProc"] for t in range(makespan))

    taux = (energie_consommee / energie_disponible if energie_disponible > 0 else 0)
    
    return {
        "temps_attente_moyen": round(attente, 2),
        "temps_reponse_moyen": round(reponse, 2),
        "makespan": makespan,
        "energie_consomme_totale": energie_consommee,
        "energie_disponible_totale": energie_disponible,
        "taux_utilisation": round(taux, 4)
    }


def ecrire_metriques(metriques, algorithme, fichier):
    """
    Ecris les métriques dans le fichier csv
    """

    colonnes = [
        "algorithme",
        "temps_attente_moyen",
        "temps_reponse_moyen",
        "makespan",
        "energie_consomme_totale",
        "energie_disponible_totale",
        "taux_utilisation"
    ]

    os.makedirs(os.path.dirname(fichier) or ".", exist_ok=True)

    lignes = []

    if os.path.exists(fichier):
        with open(fichier, "r", newline="", encoding="utf-8") as f:
            lignes = [l for l in csv.DictReader(f) if l["algorithme"] != algorithme]

    lignes.append({"algorithme": algorithme, **metriques})

    with open(fichier, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=colonnes)
        writer.writeheader()
        writer.writerows(lignes)


def ecrire_resultats(processus, ressources, energie, algorithme, fichier_global, fichier_allocations, fichier_metriques, allocations=None):
    """
    Ecris les résultats de l'exécution dans les fichiers respectifs
    :param processus : le fichier processus.csv
    :param ressources : ressources.json
    :param energie : energie.csv
    :param algorithme : le nom de l'algorithme testé (ex: "FIFO")
    :param fichier_global : chemin du fichier resultats_fifo_global.csv
    :param fichier_allocations : chemin du fichier resultats_fifo_allocations.csv
    :param fichier_metriques : chemin du fichier metriques.csv
    :param allocations : (facultatif) un élément par passage sur un processeur.
                         FIFO : ne rien donner (un processus = une allocation).
                         Round-Robin : donner l'historique renvoyé par l'algorithme.
    :return: les métriques sous forme de dictionnaire
    """

    if allocations is None:
        allocations = processus

    print(f"\nRésultats de {algorithme}")

    erreurs = verifier_contraintes(allocations, ressources, energie)

    if erreurs:
        print("Contraintes non respectées :")
        for erreur in erreurs:
            print(erreur)
    else:
        print("Toutes les contraintes sont respectées.")

    # Allocation générale
    ecrire_csv(processus, fichier_global, [
        "id_processus",
        "date_soumission",
        "date_debut",
        "date_fin",
        "ram_necessaire"
    ])

    # Allocation détaillée
    ecrire_csv(allocations, fichier_allocations, [
        "id_processus",
        "date_debut",
        "date_fin",
        "processeur"
    ])

    # Calcul et enregistrement des métriques
    metriques = calculer_metriques(processus, ressources, energie, allocations)

    ecrire_metriques(metriques, algorithme, fichier_metriques)

    print("Fichiers générés avec succès !")

    return metriques
