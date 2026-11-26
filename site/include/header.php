<header class="header py-3">
    <!-- conteneur principal du header -->
    <div class="container-fluid px-4 d-flex align-items-center justify-content-between header-bar">
            
        <!-- Logo à gauche -->
        <a href="index.php" class="header-logo d-flex align-items-center">
            <img src="images/logo.png" alt="Logo Pokéd'Aix" height="58">
        </a>

        <!-- Titre centré -->
        <p class="header-title mb-0 text-center flex-grow-1">Pokéd'Aix</p>
            
        <!-- Logos Connexion et Panier à droite -->
        <div class="d-flex align-items-center">
            <!-- Lien vers la page de connexion / compte -->
            <a href="connexion.php" class="header-icon ml-2" title="Compte">
                <img src="images/user.png" alt="Connexion" height="24">
            </a>

            <!-- Lien vers le panier -->
            <a href="panier.php" class="header-icon ml-2 position-relative" title="Panier">
                <img src="images/panier.png" alt="Panier" height="24">
            </a>
        </div>
    </div>

    <!-- Barre de recherche centrée-->
    <div class="row justify-content-center mt-2">
        <div class="col-12 col-md-7 col-lg-5 px-3">
            <form action="recherche.php" method="GET">
                <div class="input-group search-group">
                    <input type="text" name="q" class="form-control" placeholder="Rechercher sur Pokéd'Aix..." aria-label="Rechercher">
                    <div class="input-group-append">
                        <button class="btn btn-recherche" type="submit">Rechercher</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</header>