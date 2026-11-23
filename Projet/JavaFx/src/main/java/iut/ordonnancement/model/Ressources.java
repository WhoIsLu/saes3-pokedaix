package iut.ordonnancement.model;

import java.util.List;

public class Ressources {

    private int nbProcesseurs;
    private int ramTotale;
    private int energieParProc;
    private List<String> processeur;

    public int getNbProcesseurs() {
        return nbProcesseurs;
    }

    public int getRamTotale() {
        return ramTotale;
    }

    public int getEnergieParProc() {
        return energieParProc;
    }

    public List<String> getProcesseur() {
        return processeur;
    }

    public void setNbProcesseurs(int nbProcesseurs) {
        this.nbProcesseurs = nbProcesseurs;
    }

    public void setRamTotale(int ramTotale) {
        this.ramTotale = ramTotale;
    }

    public void setEnergieParProc(int energieParProc) {
        this.energieParProc = energieParProc;
    }

    public void setProcesseur(List<String> processeur) {
        this.processeur = processeur;
    }
}
