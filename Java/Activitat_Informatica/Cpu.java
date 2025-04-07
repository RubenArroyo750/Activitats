package Activitat_Informatica;

public class Cpu extends Article{
    private float velocitat;

    public Cpu(String codi, String descripcio, int unitats, float preuBase, float velocitat) {
        super(codi, descripcio, unitats, preuBase);
        this.velocitat = velocitat;
    }

    public float preu(){
        float preuFinal = getPreuBase() * velocitat;
        return preuFinal;
    }

    public float getVelocitat() {
        return velocitat;
    }

    @Override
    public String toString() {
        return String.format("%-5s %-15s %5d %10.1f %8.1f", codi, descripcio, unitats, velocitat, preu());
    }
}
