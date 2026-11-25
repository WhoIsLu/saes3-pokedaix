package iut.ordonnancement.controller;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.Node;
import javafx.scene.control.Alert;
import javafx.stage.Stage;

public class MainViewController {

@FXML
private void ouvrirConfiguration() {

}

@FXML
private void ouvrirAffichage(ActionEvent event) {
    try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/iut/ordonnancement/fxml/AffichageView.fxml"));
            Parent root = loader.load();

            Stage stage = (Stage) ((Node) event.getSource()).getScene().getWindow();

            Scene scene = new Scene(root);

            stage.setScene(scene);
            stage.setTitle("Configuration de l'ordonnanceur");

            stage.show();

        } catch (Exception e) {
            e.printStackTrace();
        }
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