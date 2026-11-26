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
                <label for="menu-1" class="menu-trigger menu-open">menu 1</label>
                <label for="menu-none" class="menu-trigger menu-close">menu 1</label>
            </li>
            <li class="nav-item px-1 menu-item-2">
                <label for="menu-2" class="menu-trigger menu-open">menu 2</label>
                <label for="menu-none" class="menu-trigger menu-close">menu 2</label>
            </li>
            <li class="nav-item px-1 menu-item-3">
                <label for="menu-3" class="menu-trigger menu-open">menu 3</label>
                <label for="menu-none" class="menu-trigger menu-close">menu 3</label>
            </li>
            <li class="nav-item px-1 menu-item-4">
                <label for="menu-4" class="menu-trigger menu-open">menu 4</label>
                <label for="menu-none" class="menu-trigger menu-close">menu 4</label>
            </li>
        </ul>

        <div class="submenu-wrapper">
            <div class="submenu-content submenu-1">
                <a href="menu1_1.php">Sous-menu 1.1</a>
                <a href="menu1_2.php">Sous-menu 1.2</a>
            </div>
            <div class="submenu-content submenu-2">
                <a href="menu2_1.php">Sous-menu 2.1</a>
                <a href="menu2_2.php">Sous-menu 2.2</a>
            </div>
            <div class="submenu-content submenu-3">
                <a href="menu3_1.php">Sous-menu 3.1</a>
                <a href="menu3_2.php">Sous-menu 3.2</a>
            </div>
            <div class="submenu-content submenu-4">
                <a href="menu4_1.php">Sous-menu 4.1</a>
                <a href="menu4_2.php">Sous-menu 4.2</a>
            </div>
        </div>
    </div>
</nav>
