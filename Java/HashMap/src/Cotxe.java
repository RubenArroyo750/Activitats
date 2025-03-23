public class Cotxe {
    private String marca;
    private String model;
    private double cilindrada;
    private float potencia;
    private Transmissio transmissio;
    private boolean hibrid;

    enum Transmissio {
        Manual, Automatic;
    }

    public Cotxe(String marca, String model, double cilindrada, float potencia, Transmissio transmissio, boolean hibrid) {
        this.marca = marca;
        this.model = model;
        this.cilindrada = cilindrada;
        this.potencia = potencia;
        this.transmissio = transmissio;
        this.hibrid = hibrid;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public double getCilindrada() {
        return cilindrada;
    }

    public void setCilindrada(double cilindrada) {
        this.cilindrada = cilindrada;
    }

    public float getPotencia() {
        return potencia;
    }

    public void setPotencia(float potencia) {
        this.potencia = potencia;
    }

    public Transmissio getTransmissio() {
        return transmissio;
    }

    public void setTransmissio(Transmissio transmissio) {
        this.transmissio = transmissio;
    }

    public boolean isHibrid() {
        return hibrid;
    }

    public void setHibrid(boolean hibrid) {
        this.hibrid = hibrid;
    }

    // Mètode per mostrar les dades del cotxe
    public String toString() {
        return "Marca: " + marca + "\n" +
                "Model: " + model + "\n" +
                "Cilindrada: " + cilindrada + "\n" +
                "Potencia: " + potencia + "\n" +
                "Transmissio:  " + transmissio + "\n" +
                "Hibrid: " + (hibrid ? "Si" : "No");

    }
}

