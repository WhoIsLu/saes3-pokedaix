from Ordonnancement.Contraintes import contrainteRAM, contrainteEnergie

def ordonancementRoundRobin(processus: list, ressources: dict, energie: list, quantum: int) -> list:
    # Tri initial de la liste : soumission croissante, priorité décroissante
    processus.sort(key=lambda x: (x["date_soumission"], -x["priorite"]))
    
    # Préparation des listes
    file_attente = []
    termines = []
    
    # Historique complet pour Vincent (puisqu'un processus RR peut s'asseoir plusieurs fois)
    # On ajoute ce tableau spécifique au RR pour qu'il ait toutes les découpes
    historique_allocations = []
 
    # Suivi des processeurs : {"CPU1": None, "CPU2": None}
    cpus = {}
    for cpu in ressources["processeur"]:
        cpus[cpu] = None
        
    t = 0
    processus_restants = processus.copy()

    # Boucle principale : tourne tant que tout n'est pas terminé
    while len(termines) < len(processus):
        
        # 1. Fait entrer les processus soumis à l'instant t dans la file d'attente
        for p in list(processus_restants):
            if p["date_soumission"] == t:
                # Ajout d'un compteur spécifique au RR : temps passé sur ce CPU actuel
                file_attente.append(dict(p, temps_restant=p["duree_execution"], temps_sur_cpu=0, date_debut=None, date_fin=None, processeur=None))
                processus_restants.remove(p)

        # 2. Gestion des sorties (Fin de tâche ou Quantum écoulé) AVANT de placer de nouveaux processus
        for cpu, p in cpus.items():
            if p is not None:
                # Si le processus vient de terminer
                if p["temps_restant"] == 0:
                    historique_allocations.append({
                        "processus": p["nom"], "cpu": cpu, 
                        "debut": p["date_debut"], "fin": t
                    })
                    p["date_fin"] = t
                    termines.append(p)
                    cpus[cpu] = None
                    
                # Si le processus n'a pas fini, mais que son quantum est écoulé
                elif p["temps_sur_cpu"] == quantum:
                    historique_allocations.append({
                        "processus": p["nom"], "cpu": cpu, 
                        "debut": p["date_debut"], "fin": t
                    })
                    p["temps_sur_cpu"] = 0 # Remise à zéro de son compteur local
                    p["date_debut"] = None # Il n'a plus de date de début "actuelle"
                    p["processeur"] = None
                    file_attente.append(p) # Retourne faire la queue
                    cpus[cpu] = None

        # 3. Calcul de la RAM et de l'énergie disponibles
        ram_utilisee = 0
        cpus_occupes = 0
        for p in cpus.values():
            if p is not None:
                ram_utilisee += p["ram_necessaire"]
                cpus_occupes += 1

        energie_actuelle = 0
        for e in energie:
            if e["instant"] == t:
                energie_actuelle = e["energie_disponible"]
                break

        cpus_possibles = contrainteEnergie(energie_actuelle, ressources["energieParProc"], ressources["nbProcesseurs"])
        
        # 4. Coupure d'énergie : on éjecte les processus si l'énergie chute brutalement
        if cpus_occupes > cpus_possibles:
            cpt_a_ejecter = cpus_occupes - cpus_possibles
            for cpu, p in cpus.items():
                if p is not None and cpt_a_ejecter > 0:
                    historique_allocations.append({
                        "processus": p["nom"], "cpu": cpu, 
                        "debut": p["date_debut"], "fin": t
                    })
                    p["temps_sur_cpu"] = 0
                    p["date_debut"] = None
                    p["processeur"] = None
                    file_attente.insert(0, p) # Remis en priorité absolue devant la file
                    cpus[cpu] = None
                    cpt_a_ejecter -= 1
                    cpus_occupes -= 1
                    ram_utilisee -= p["ram_necessaire"]
        
        # 5. Parcours de la file d'attente pour assigner les processus
        for p in list(file_attente):
            cpu_libre = None
            for cpu, occupant in cpus.items():
                if occupant is None:
                    cpu_libre = cpu
                    break
            
            if not cpu_libre:
                break  
            
            # Vérification si on a le droit d'allumer une machine et si la RAM passe
            if cpus_occupes < cpus_possibles and contrainteRAM(ressources, p, ram_utilisee):
                p["date_debut"] = t # L'heure à laquelle il s'assoit pour ce tour
                p["processeur"] = cpu_libre
                cpus[cpu_libre] = p
                ram_utilisee += p["ram_necessaire"]
                cpus_occupes += 1
                file_attente.remove(p)

        # 6. Avancée du temps (Pas de temps +1)
        # On diminue le temps restant et on augmente le temps passé sur la machine
        for cpu, p in cpus.items():
            if p is not None:
                p["temps_restant"] -= 1
                p["temps_sur_cpu"] += 1
                
        t += 1
        
        # Sécurité infinie
        if t > 5000:
            print("Boucle infinie détectée")
            break

    # Pour l'export final, on renvoie à la fois les processus terminés ET l'historique complet des coupures
    return termines, historique_allocations
