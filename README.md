# SAÉ S3 — Système d'Information e-commerce Pokéd'Aix
**Équipe MOE (groupe 1B4)** — Lucie MACHIAVELLI, Anas OUQUA, Théo SONNEVILLE, Vincent PACORET
**Client (MOA)** — Pokéd'Aix SAS, boutique de cartes à collectionner à Aix-en-Provence

Le projet comprend trois modules qui partagent la même base de données :
- **Site web** (PHP 8, MVC, PDO) : site client + console d'administration ;
- **Base de données** (SQL) : schéma, contraintes, procédures stockées et triggers ;
- **Ordonnancement** (Python) + **interface de visualisation** (JavaFX).

## Sommaire
1. [Présentation de l'équipe](#présentation-de-léquipe)
2. [Planning des sprints](#planning-des-sprints)
3. [Répartition des tâches et état d'avancement](#répartition-des-tâches-et-état-davancement)
4. [Tests](#tests)
5. [Arborescence du dépôt](#arborescence-du-dépôt)
6. [Livrables et jalons officiels](#livrables-et-jalons-officiels)
7. [Bilan individuel par sprint](#bilan-individuel-par-sprint)

---

## Présentation de l'équipe

Les rôles Scrum changent à chaque période de deux semaines.

| Membre | Sem 45-46 (Sprint 0) | Sem 47-48 (Sprint 1) | Sem 49-50 (Sprint 2) |
| :--- | :--- | :--- | :--- |
| Lucie | Scrum Master | Développeuse | *à définir* |
| Théo | Product Owner | Scrum Master | *à définir* |
| Anas OUQUA | Développeur | Product Owner | *à définir* |
| Vincent | Développeur | Développeur | *à définir* |

---

## Planning des sprints

| Sprint | Dates | Objectif | Milestone GitHub |
| :--- | :--- | :--- | :--- |
| Sprint 0 | jusqu'au 13/11 | Dépôt Git, backlog produit, conception (UC, classes, DSS) | `Sprint 0` |
| Sprint 1 | 16/11 → 27/11 | BD (conception), charte graphique, SEP, module Python | `Sprint 1` |
| Sprint 2 | 30/11 → 11/12 | Compte client, panier, script BD, interface JavaFX | `Sprint 2` |
| Sprint 3 | 14/12 → 08/01 | Commande, paiement, avis, procédures stockées et triggers | `Sprint 3` |
| Recette | 11/01 → 14/01 | Tests et corrections | — |

Le suivi détaillé se fait dans le **Project Board** GitHub : une issue par user story (US), découpée en tâches (task list).

---

## Répartition des tâches et état d'avancement

### Sprint 1 (16/11 → 27/11) : tâches du sprint

**Base de données** (rendu le 29/11)

| Tâche | Responsable | État | Livrable |
| :--- | :--- | :--- | :--- |
| Diagramme de classes | Vincent, Lucie | En cours | [`bd/`](bd/) |
| Dictionnaire de données | Anas | Fait | [`bd/`](bd/) |
| Schéma relationnel | Lucie | Fait | [`bd/`](bd/) |

**Site web** (rendu le 29/11)

| Tâche | Responsable | État | Livrable |
| :--- | :--- | :--- | :--- |
| Charte graphique (`index.php` + include) | Théo | Fait | [`site/`](site/) |
| SEP + diagramme d'état de la commande | Vincent | En cours | [`docs/`](docs/) |
| Maquettes | Équipe | En cours | [`maquettes/`](maquettes/) |

**Module Python : ordonnancement** (rendu le 06/12)

| Fichier | Rôle | Responsable | État |
| :--- | :--- | :--- | :--- |
| `lecture.py` | Lecture de `config.txt`, des CSV et de `ressources.json` | Lucie | Fait |
| `Ordonnancement/Contraintes.py` | Contraintes de RAM et d'énergie (`contrainteRAM`, `contrainteEnergie`) | Théo, Anas | Fait |
| `Ordonnancement/FIFO.py` | Politique FIFO | Théo | Fait |
| `Ordonnancement/RoundRobin.py` | Politique Round-Robin (quantum, historique des passages sur CPU) | Anas | En test |
| `ecriture.py` | Fichiers de résultats, vérification des contraintes, métriques | Vincent | En test |
| `main.py` | Lancement de la simulation (`config.txt` → algorithmes → résultats) | Lucie | En cours |

Points restant à traiter avant le rendu :
- `main.py` ne traite que `Test01` : il faut aussi traiter `Test02` et écrire dans `Outputs/Test01/`, `Outputs/Test02/` (structure imposée par le sujet) ;
- `main.py` : passer `allocations=historique` à `ecrire_resultats` pour le Round-Robin ;
- `lecture.py` : placer les `print` de test sous `if __name__ == "__main__":`.

### Sprint 2 (30/11 → 11/12) : prévisionnel

| Tâche | Module | Responsable | État |
| :--- | :--- | :--- | :--- |
| Script de création de la BD + insertions (rendu 06/12) | BD | *à répartir* | À faire |
| Authentification, sessions, mots de passe hachés (rendu 06/12) | Site PHP | *à répartir* | À faire |
| Interface JavaFX : création/modification du fichier de configuration | Java | Anas, Vincent, Lucie | À faire |
| Interface JavaFX : lancement de l'application Python | Java | *à répartir* | À faire |
| Interface JavaFX : diagramme de Gantt par processeur | Java | Anas | À faire |
| Documentation technique + Javadoc (rendu 07/12) | Java | Équipe | À faire |

---

## Tests

### Module Python

- **Jeux de test** : `Projet/python/Inputs/Test01` et `Test02` (`config.txt`, `processus.csv`, `ressources.json`, `energie.csv`).
- **Lancement** (depuis le dossier `Code`) :
```bash
  cd Projet/python/Code
  python main.py
```
- **Vérifications automatiques** : `ecriture.py` contrôle, à chaque instant, que la RAM utilisée et le nombre de processeurs allumés respectent les contraintes, puis affiche « Toutes les contraintes sont respectées ».
- **Test du Round-Robin calculé à la main** : 2 CPU, quantum 2, 3 processus (P1 et P2 arrivent à t = 0, P3 à t = 1).
  Résultat attendu et obtenu : P2 0 → 2 ; P1 0 → 2 puis 2 → 3 ; P3 2 → 4 puis 4 → 5 ; makespan = 5.
- **Test01** : FIFO et Round-Robin respectent toutes les contraintes. Pic de RAM vérifié pour le Round-Robin : 1024 sur 1024.

### Site web et BD
*À compléter au fil des sprints : traces d'exécution SQL et PHP, puis cahier de recette (sprint 3).*

---

## Arborescence du dépôt

```
saes3-pokedaix/
├── bd/                     Conception de la BD (diagramme de classes, dictionnaire, schéma relationnel)
├── docs/                   Documentation (backlog, revues de sprint, SEP…)
├── maquettes/              Maquettes du site
├── site/                   Site web PHP (charte graphique, pages)
├── Projet/
│   ├── JavaFx/             Interface de visualisation
│   └── python/
│       ├── Code/           main.py, lecture.py, ecriture.py, Ordonnancement/
│       ├── Inputs/         Test01/, Test02/
│       └── Outputs/        Fichiers de résultats générés
├── BackLog Produit.csv
└── README.md
```

---

## Livrables et jalons officiels

| Date | Livrable | Lien |
| :--- | :--- | :--- |
| 13/11/2026 | Backlog produit et planning des sprints | [`BackLog Produit.csv`](BackLog%20Produit.csv) |
| 29/11/2026 | BD : diagramme de classes, dictionnaire de données, schéma relationnel | [`bd/`](bd/) |
| 29/11/2026 | PHP : charte graphique et SEP | [`site/`](site/) |
| 06/12/2026 | Python : code, fichiers de tests, résultats et README | [`Projet/python/`](Projet/python/) |
| 06/12/2026 | BD : script de création + insertions | [`bd/`](bd/) |
| 06/12/2026 | PHP : authentification, sessions, mots de passe chiffrés | [`site/`](site/) |
| 07/12/2026 | Java : code, documentation technique et Javadoc | [`Projet/JavaFx/`](Projet/JavaFx/) |
| 11/12/2026 | Fin du sprint 2 | Release `v0.2` |
| 13/12/2026 | BD : procédures stockées et triggers | [`bd/`](bd/) |
| 08/01/2027 | Fin du sprint 3 | Release `v0.3` |
| 15/01/2027 | Livraison finale (site + BD, cahier de recette, documentations) | Release `v1.0` |

---

## Bilan individuel par sprint

Chaque membre complète sa ligne à la fin du sprint. Le détail au jour le jour est visible dans les commits et les issues GitHub.

### Sprint 0 (03/11 → 15/11) : mise en place et conception

| Membre | Travail réalisé | Issues / fichiers |
| :--- | :--- | :--- |
| Lucie | | |
| Anas OUQUA | | |
| Théo | | |
| Vincent | | |

### Sprint 1 (16/11 → 27/11) : BD, charte graphique, module Python

| Membre | Travail réalisé | Issues / fichiers |
| :--- | :--- | :--- |
| Lucie | | |
| Anas OUQUA | | |
| Théo | | |
| Vincent | | |
