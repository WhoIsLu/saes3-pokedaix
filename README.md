# SAÉ S3 — Système d'Information e-commerce Pokéd'Aix
**Équipe MOE** — Lucie, Anas OUQUA, Théo, Vincent

## Présentation de l'équipe

| Membre | Sem 45-46 | Sem 47-48 | Sem 49-50 |
| :--- | :--- | :--- | :--- |
| Lucie | SCRUM Master | Développeuse |  |
| Théo | Product Owner | SCRUM Master |  |
| Anas OUQUA | Développeur | Product Owner |  |
| Vincent | Développeur | Développeur |  |

## Travail personnel (Journal de bord)

A remplir à chaque fois qu'on travaille

| Date | Lucie | Anas OUQUA | Théo | Vincent |
| :--- | :--- | :--- | :--- | :--- |
| 03/11 | Création du repository GitHub et du README de base | | | Début des histoires techniques et du diagramme de classes métier |
| 04/11 | Création du Project Board Scrum et des Jalons (Sprints 0 à 3) | | Création du backlog produit et intégration des user stories | Réalisation du diagramme de cas d'utilisation (UC) |
| 08/11 | Création, découpage et estimation des Issues US01 à US08 (Catalogue) | Création, découpage et estimation des Issues US16-US22 (Panier/Paiement) et US24, US27-US31 (Stocks Java) | Création, découpage et estimation des Issues US09-US15 (Comptes) et US23, 25, 26 (Admin) | Création, découpage et estimation des Issues US32-US35 (Python Data) |
| 10/11 | Poker de complexité du backlog et remplissage du Sprint 1 | Poker de complexité du backlog et remplissage du Sprint 1 | Poker de complexité du backlog et remplissage du Sprint 1 | Diagrammes de séquence (DSS) et finalisation du diagramme de classes |
| 11/11 | | | Envoi du backlog complété à la MOA pour validation | |
| 12/11 | Développement de `lecture.py` pour parser les fichiers `.csv` et `.txt` | Conception mathématique des fonctions partagées d'énergie (`math.floor`) | Rédaction de la logique RAM partagée (`contrainteRAM`) | Préparation des fonctions de formatage et de récupération de l'historique d'allocation |
| 14/11 | Mise en place de l'arborescence stricte avec les sous-dossiers `Inputs/Test01` et `Outputs/Test01` | Mise à jour de l'arborescence locale et session d'entraide sur les squelettes de `Contraintes.py` | Écriture du squelette de `FIFO.py` et début du fichier `Contraintes.py` | Création du squelette des fichiers d'export et tests d'écriture |
| 15/11 | Intégration de la liste d'énergie dans la boucle principale | Finalisation de `contrainteEnergie`, session VS Code Live Share et rédaction du README final | Correction de `contrainteRAM` avec Anas via Live Share | Tests de création des fichiers `.csv` de sortie dans le répertoire `Outputs/Test01` |

## Répartition des tâches et état d'avancement

| version | rôle utilisateur | use case | fonctionnalité | Lucie | Anas OUQUA | Théo | Vincent |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| V1 | Gérant | Gestion des ressources | Définir la contrainte d'énergie disponible | | F | F | |
| V1 | Gérant | Gestion des ressources | Définir la contrainte de RAM disponible | | F | F | |
| V1 | Système | Ordonnancement | Exécuter la politique FIFO | | | F | |
| V1 | Système | Ordonnancement | Exécuter la politique Round-Robin | | F | | |
| V1 | Système | Intégration | Lancer la simulation globale (`main.py`) | F | | | |
| V1 | Gérant | Suivi des résultats | Exporter l'historique global et détaillé en CSV | | | | F |
| V1 | Gérant | Suivi des résultats | Calculer les métriques comparatives des politiques | | | | F |
| V1 | - | Documentation | Rédaction du README du dépôt Git | | F | | |
| V2 | Visiteur | Catalogue Web (PHP) | Naviguer dans les catégories et filtrer les produits | F | | | |
| V2 | Vendeur | Application Boutique (Java) | Gérer les stocks et réceptionner les fournisseurs | | F | | |
| V2 | Client | Tunnel d'achat (PHP) | Ajouter au panier, choisir livraison et payer | | F | | |
| V2 | Gérant | Administration (PHP) | Modération des avis et gestion des lots | | | F | |
| V2 | Gérant | Analyse (Python) | Générer un tableau de bord des ventes (pandas) | | | | F |

## Livrables et Jalons Officiels

| Date | Nom | Lien |
| :--- | :--- | :--- |
| 13/11/2026 | Backlog produit & Planning des sprints | [Backlog & Planning](docs/planning/Backlog_Planning.md) |
| 27/11/2026 | Sprint 1 : BDD, Catalogue, Maquettes | [Revue Sprint 1](docs/sprint1/Sprint1_Review.md) |
| 29/11/2026 | Livrable PHP 1 : Charte graphique et SEP | [Dossier Site PHP](site/) |
| 11/12/2026 | Sprint 2 : Compte client, Panier, App Java | [Revue Sprint 2](docs/sprint2/Sprint2_Review.md) |
| 08/01/2027 | Sprint 3 : Commande, Scripts Python complets | [Module Python (Ordonnancement & Analyse)](python/Code/) |
| 15/01/2027 | Livraison finale (Code, Doc Utilisateur, Doc Technique) | [Dossier complet des Livrables Finaux](docs/) |
