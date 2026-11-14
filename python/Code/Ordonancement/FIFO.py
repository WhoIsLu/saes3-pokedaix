from Code.Ordonancement.Contraintes import contrainteRAM, contrainteEnergie

def ordonancementFIFO(processus: list, ressources: dict, energie: list) -> list:
    # Tri initial de le liste : soumission croissante, priorité décroissante
    processus.sort(key=lambda x: (x["date_soumission"], -x["priorite"]))
    
    # Préparation des listes et copies de processus
    file_attente = []
    termines = []
 
    # Suivi des processeurs : {"CPU1": None, "CPU2": None}
    cpus = {}
    for cpu in ressources["processeur"]:
        cpus[cpu] = None
    t = 0

    # Boucle principale
    while len(termines) < len(processus):
        # Fait entrer les processus soumis à l'instant t dans la file d'attente
        for p in processus:
            if p["date_soumission"] == t:
                file_attente.append(dict(p, temps_restant=p["duree_execution"], date_debut=None, date_fin=None, processeur=None))

        # initialise la ram utilisée et le nombre de CPU occupés
        ram_utilisee = 0
        cpus_occupes = 0
        for p in cpus.values():
            if p is not None:
                ram_utilisee += p["ram_necessaire"]
                cpus_occupes += 1

        
        # Récupération de l'énergie disponible à l'instant t
        energie_actuelle = 0
        for e in energie:
            if e["instant"] == t:
                energie_actuelle = e["energie_disponible"]
                break

        # Calcul du nombre de processeurs disponnibles
        cpus_possibles = contrainteEnergie(energie_actuelle, ressources["energieParProc"], ressources["nbProcesseurs"])
        
        # Parcours de la file d'attente pour assigner les processus aux CPU disponibles
        for p in list(file_attente):
            # Cherche le premier CPU libre
            cpu_libre = None
            for cpu, occupant in cpus.items():
                if occupant is None:
                    cpu_libre = cpu
                    # si on a un cpu de libre, pas besoin d'aller voir les suivants
                    break
            # Si plus de CPU disponible à cet instant, on quit la boucle
            if not cpu_libre:
                break  
            # Vérification si il reste assez de CPU et de RAM avant d'assigner le processus
            if cpus_occupes < cpus_possibles and contrainteRAM(ressources, p, ram_utilisee):
                p["date_debut"] = t
                p["processeur"] = cpu_libre
                cpus[cpu_libre] = p
                ram_utilisee += p["ram_necessaire"]
                cpus_occupes += 1
                file_attente.remove(p)

        # Pas de temps +1 et libération des CPU pour les processus finis
        t += 1
        for cpu, p in cpus.items():
            if p is not None:
                p["temps_restant"] -= 1
                if p["temps_restant"] == 0:
                    p["date_fin"] = t
                    termines.append(p)
                    cpus[cpu] = None

    return termines
