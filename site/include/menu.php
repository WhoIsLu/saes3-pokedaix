<!-- Barre de navigation -->
<nav class="navbar">
    <div class="container-fluid flex-column px-3">
        <!-- Radios cachés pour gérer l'ouverture/fermeture exclusive sans JavaScript -->
        <input type="radio" name="menu-toggle" id="menu-none" class="menu-radio" checked>
        <input type="radio" name="menu-toggle" id="menu-1" class="menu-radio">
        <input type="radio" name="menu-toggle" id="menu-2" class="menu-radio">
        <input type="radio" name="menu-toggle" id="menu-3" class="menu-radio">
        <input type="radio" name="menu-toggle" id="menu-4" class="menu-radio">

        <ul class="nav nav-links nav-justified">
            <li class="nav-item px-1">
                <a href="index.php">Accueil</a>
            </li>
            <li class="nav-item px-1 menu-item-1">
                <label for="menu-1" class="menu-trigger menu-open">Univers/licence</label>
                <label for="menu-none" class="menu-trigger menu-close">Univers/licence</label>
            </li>
            <li class="nav-item px-1 menu-item-2">
                <label for="menu-2" class="menu-trigger menu-open">Catalogue</label>
                <label for="menu-none" class="menu-trigger menu-close">Catalogue</label>
            </li>
            <li class="nav-item px-1 menu-item-3">
                <label for="menu-3" class="menu-trigger menu-open">Regroupements</label>
                <label for="menu-none" class="menu-trigger menu-close">Regroupements</label>
            </li>
            <li class="nav-item px-1 menu-item-4">
                <label for="menu-4" class="menu-trigger menu-open">Informations</label>
                <label for="menu-none" class="menu-trigger menu-close">Informations</label>
            </li>
        </ul>

        <div class="submenu-wrapper">
            <div class="submenu-content submenu-1">
                <a href="menu1_1.php">Pokémon</a>
                <a href="menu1_2.php">One Piece</a>
                <a href="menu1_3.php">Lorcana</a>
                <a href="menu1_4.php">Magic</a>
                <a href="menu1_5.php">Yu-Gi-Oh</a>
            </div>
            <div class="submenu-content submenu-2">
                <a href="menu2_1.php">Produits scellés</a>
                <a href="menu2_2.php">Cartes à l'unité</a>
                <a href="menu2_3.php">Accessoires</a>
                <a href="menu2_4.php">Produits dérivés</a>
                <a href="menu2_5.php">sous-catégories</a>
            </div>
            <div class="submenu-content submenu-3">
                <a href="menu3_1.php">Nouveautés</a>
                <a href="menu3_2.php">Meilleures ventes</a>
                <a href="menu3_3.php">Soldes</a>
                <a href="menu3_4.php">Lots</a>

            </div>
            <div class="submenu-content submenu-4">
                <a href="menu4_1.php">Evènements</a>
                <a href="menu4_2.php">La boutique</a>
                <a href="menu4_3.php">Garantie</a>
                <a href="menu4_4.php">Mentions légales</a>
                <a href="menu4_5.php">Confidentialité</a>
                <a href="menu4_6.php">Contact</a>
            </div>
        </div>
    </div>
</nav>
