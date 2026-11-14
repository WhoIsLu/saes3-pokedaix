import math


def contrainteRAM(ressources: dict, processus: dict, ram_actuelle: int) -> bool:
    """
    Vérifie si la RAM disponible suffit pour lancer le processus.
    Utilise 'ramTotale' fourni par lire_json().
    """
    ram_totale = ressources["ramTotale"]
    ram_demandee = processus["ram_necessaire"]
    
    return (ram_actuelle + ram_demandee) <= ram_totale

def contrainteEnergie(energie_actuelle, energie_par_cpu, nb_cpu_max):
    """
    Calcule combien de processeurs on a le droit d'allumer à cet instant,
    en fonction de l'énergie disponible.
    """
    cpus_possibles = math.floor(energie_actuelle / energie_par_cpu)
    
    if cpus_possibles > nb_cpu_max:
        return nb_cpu_max
    else:
        return cpus_possibles

def obtenirCPULibre(cpus_occupation: dict) -> str:
    """Renvoie le nom d'un processeur inoccupé (ex: 'CPU1') ou None."""
    for cpu_name, occupant in cpus_occupation.items():
        if occupant is None:
            return cpu_name
    return None
