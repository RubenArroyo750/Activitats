public class Client {
    private String nom;
    private String dni;
    private int numeroTargeta;

    public Client(String nom, String dni, int numeroTargeta) {
        this.nom = nom;
        this.dni = dni;
        this.numeroTargeta = numeroTargeta;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public String getDni() {
        return dni;
    }

    public void setDni(String dni) {
        this.dni = dni;
    }

    public int getNumeroTargeta() {
        return numeroTargeta;
    }

    public void setNumeroTargeta(int numeroTargeta) {
        this.numeroTargeta = numeroTargeta;
    }
}
