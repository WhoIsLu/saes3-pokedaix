package iut.ordonnancement.controller;

import javafx.fxml.FXML;
import javafx.event.ActionEvent;
import javafx.scene.control.Alert;
import javafx.scene.control.MenuBar;
import javafx.stage.Stage;

public class MainViewController {

    @FXML 
    private MenuBar menuBar;

    @FXML
    private void fermer(ActionEvent event) {
        Stage stage = (Stage) menuBar.getScene().getWindow();
        stage.close();
    }

    @FXML
    private void afficherAbout() {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("À propos");
        alert.setHeaderText("Ordonnanceur");
        alert.setContentText("Application d'ordonnancement");
        alert.showAndWait();
    }


}