package iut.ordonnancement.model;

public class Energie {

    private int instant;
    private int energieDisponible;

    public Energie(int instant, int energieDisponible) {
        this.instant = instant;
        this.energieDisponible = energieDisponible;
    }

    public int getInstant() {
        return instant;
    }

    public int getEnergieDisponible() {
        return energieDisponible;
    }
}
