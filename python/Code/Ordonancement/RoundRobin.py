from Ordonnancement.Contraintes import contrainteEnergie, contrainteRAM, obtenirCPULibre

def executer_round_robin(liste_processus, liste_energie, nb_cpu_total, ressources, quantum, energie_par_cpu):
    """
    Simule l'ordonnancement Round-Robin avec contraintes d'énergie et de RAM.
    Renvoie l'historique des allocations pour l'export de données.
    """
    temps = 0
    file_attente = []
    historique_allocations = []
    
    # Représentation de nos machines (ex: {'CPU1': None, 'CPU2': dict_du_processus})
    cpus_occupation = {f"CPU{i+1}": None for i in range(nb_cpu_total)}
    processus_non_arrives = liste_processus.copy()
    
    # La boucle tourne tant qu'il reste des processus à traiter, en attente, ou sur les machines
    while processus_non_arrives or file_attente or any(cpus_occupation.values()):
        
        # 1. ARRIVÉES : on fait entrer les processus dont c'est l'heure
        arrivants = [p for p in processus_non_arrives if p.get("date_arrivee", 0) == temps]
        for p in arrivants:
            p["temps_restant"] = p["duree_execution"]
            p["temps_passe_sur_cpu"] = 0
            file_attente.append(p)
            processus_non_arrives.remove(p)

        # 2. SORTIES : Fin d'exécution ou Quantum écoulé
        for cpu, occupant in cpus_occupation.items():
            if occupant is not None:
                # Le temps de la boucle précédente vient de s'écouler pour lui
                occupant["temps_restant"] -= 1
                occupant["temps_passe_sur_cpu"] += 1
                
                # A. Le processus a terminé son travail
                if occupant["temps_restant"] <= 0:
                    historique_allocations.append({
                        "processus": occupant["nom"],
                        "cpu": cpu,
                        "debut": occupant["heure_debut_allocation"],
                        "fin": temps
                    })
                    cpus_occupation[cpu] = None
                    
                # B. Le processus a épuisé son temps (Quantum)
                elif occupant["temps_passe_sur_cpu"] >= quantum:
                    historique_allocations.append({
                        "processus": occupant["nom"],
                        "cpu": cpu,
                        "debut": occupant["heure_debut_allocation"],
                        "fin": temps
                    })
                    # On remet son chronomètre local à zéro et il retourne faire la queue
                    occupant["temps_passe_sur_cpu"] = 0
                    file_attente.append(occupant)
                    cpus_occupation[cpu] = None

        # 3. GESTION DE L'ÉNERGIE
        # On vérifie la météo énergétique à la seconde actuelle
        energie_actuelle = liste_energie[temps] if temps < len(liste_energie) else 0
        cpus_autorises = contrainteEnergie(energie_actuelle, energie_par_cpu, nb_cpu_total)
        cpus_actifs = sum(1 for occ in cpus_occupation.values() if occ is not None)
        
        # Coupure de courant : on éjecte les processus en trop si l'énergie chute brutalement
        if cpus_actifs > cpus_autorises:
            cpt_a_ejecter = cpus_actifs - cpus_autorises
            for cpu, occupant in cpus_occupation.items():
                if occupant is not None and cpt_a_ejecter > 0:
                    historique_allocations.append({
                        "processus": occupant["nom"],
                        "cpu": cpu,
                        "debut": occupant["heure_debut_allocation"],
                        "fin": temps
                    })
                    occupant["temps_passe_sur_cpu"] = 0
                    # On le remet en priorité absolue devant la file car il a été coupé injustement
                    file_attente.insert(0, occupant) 
                    cpus_occupation[cpu] = None
                    cpt_a_ejecter -= 1
                    cpus_actifs -= 1

        # 4. PLACEMENT (Contrainte RAM)
        # On calcule la RAM déjà prise par les machines allumées
        ram_utilisee = sum(occ["ram_necessaire"] for occ in cpus_occupation.values() if occ is not None)
        
        # Tant qu'on a des gens qui attendent et de l'énergie pour allumer une machine
        while file_attente and cpus_actifs < cpus_autorises:
            cpu_libre = obtenirCPULibre(cpus_occupation)
            if cpu_libre is None:
                break # Plus de machines physiques disponibles
            
            candidat = file_attente[0]
            
            # Utilisation de la fonction de Théo
            if contrainteRAM(ressources, candidat, ram_utilisee):
                processus_a_placer = file_attente.pop(0)
                # On marque l'heure exacte à laquelle il s'assoit pour Vincent
                processus_a_placer["heure_debut_allocation"] = temps
                cpus_occupation[cpu_libre] = processus_a_placer
                
                ram_utilisee += processus_a_placer["ram_necessaire"]
                cpus_actifs += 1
            else:
                # Si le 1er de la file n'a pas assez de RAM, la file est bloquée (logique FIFO stricte)
                break
                
        # 5. LE CHRONOMÈTRE AVANCE
        temps += 1
        
        # Sécurité pour ne pas faire exploser votre terminal en cas de fichier mal lu
        if temps > 10000:
            print("Arrêt de sécurité : Simulation bloquée ou temps > 10000")
            break

    return historique_allocations
