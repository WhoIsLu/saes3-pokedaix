package iut.ordonnancement.controller;

import javafx.fxml.FXML;
import javafx.scene.control.Alert;

public class MainViewController {

@FXML
private void ouvrirConfiguration() {

}

@FXML
private void ouvrirAffichage() {
    
}

@FXML
private void quitterApplication() {
    javafx.application.Platform.exit();
}


@FXML
private void afficherAPropos() {

    Alert alert = new Alert(Alert.AlertType.INFORMATION);

    alert.setTitle("À propos");
    alert.setHeaderText("Visualisation des ordonnancements");

    alert.setContentText(
        "Application développée dans le cadre de la SAÉ S3.01.\n\n"
        + "Algorithmes : FIFO et Round Robin."
    );

    alert.showAndWait();
}


}