package iut.ordonnancement.model;

public class Processus {

    private String id;
    private int dateSoumission;
    private int dureeExecution;
    private int ramNecessaire;
    private int priorite;
    private int dateButoir;

    private Integer dateDebut;
    private Integer dateFin;

    public Processus(String id, int dateSoumission,
                     int dureeExecution, int ramNecessaire,
                     int priorite, int dateButoir) {

        this.id = id;
        this.dateSoumission = dateSoumission;
        this.dureeExecution = dureeExecution;
        this.ramNecessaire = ramNecessaire;
        this.priorite = priorite;
        this.dateButoir = dateButoir;
    }

    public String getId() { return id; }
    public int getDateSoumission() { return dateSoumission; }
    public int getDureeExecution() { return dureeExecution; }
    public int getRamNecessaire() { return ramNecessaire; }
    public int getPriorite() { return priorite; }
    public int getDateButoir() { return dateButoir; }

    public Integer getDateDebut() { return dateDebut; }
    public Integer getDateFin() { return dateFin; }

    public void setDateDebut(Integer dateDebut) {
        this.dateDebut = dateDebut;
    }

    public void setDateFin(Integer dateFin) {
        this.dateFin = dateFin;
    }
}
