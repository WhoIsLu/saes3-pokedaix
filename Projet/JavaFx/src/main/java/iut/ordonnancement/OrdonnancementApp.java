package iut.ordonnancement;

import java.io.IOException;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

public class OrdonnancementApp extends Application{

	public static void main2(String[] args) {
		Application.launch(args);
	}
	@Override
	public void start(Stage primaryStage) throws Exception {
		try {
			FXMLLoader loader = new FXMLLoader();
			loader.setLocation( OrdonnancementApp.class.getResource("fxml/MainView.fxml"));
			BorderPane borderPane = loader.load();  // peut lever IOEXception
			
			Scene scene = new Scene(borderPane);
			primaryStage.setScene(scene);
			primaryStage.setTitle("Ordonnancement App v2");
			primaryStage.show();
			
		} catch (IOException e) {
			System.out.println("Ressource FXML non disponible");
			e.printStackTrace(); // TODO à supprimer en prod
			System.exit(1);
		}
	}

}