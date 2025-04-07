package Activitat_Informatica;

public class DiscDur extends Article {
    private float capacitat;

    public DiscDur(String codi, String descripcio, int unitats, float preuBase, float capacitat) {
        super(codi, descripcio, unitats, preuBase);
        this.capacitat = capacitat;
    }

    public float preu(){
        float preuInicial = getPreuBase() * capacitat;
        float preuFinal = preuInicial * 0.90f; // Descompte del 10%
        return preuFinal;
    }

    public float getCapacitat() {
        return capacitat;
    }

    @Override
    public String toString() {
        return String.format("%-5s %-15s %5d %10.1f %8.1f", codi, descripcio, unitats, capacitat, preu());
    }
}
