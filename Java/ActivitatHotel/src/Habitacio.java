public class Habitacio {
    private int id;
    private String categoria;
    private int numeroLlits;
    private int preuNit;

    public Habitacio(int id, String categoria, int numeroLlits, int preuNit) {
        this.id = id;
        this.categoria = categoria.toLowerCase();
        this.numeroLlits = numeroLlits;
        this.preuNit = calcularPreu();
    }

    private int calcularPreu(){
        switch (categoria){
            case "superluxe":
                return  200;
            case "luxe":
                return  100;
            case "normal":
                return  60;
            default:
                System.out.println("La catagoria no es correcte");
                return 0;
        }
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getCategoria() {
        return categoria;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }

    public int getNumeroLlits() {
        return numeroLlits;
    }

    public void setNumeroLlits(int numeroLlits) {
        this.numeroLlits = numeroLlits;
    }

    public int getPreuNit() {
        return preuNit;
    }

    public void setPreuNit(int preuNit) {
        this.preuNit = preuNit;
    }

    public void mostrarInformacio(){
        if(preuNit != 0){
            System.out.println("Categoria de l'habitació: " + categoria);
            System.out.println("Preu per nit: " + preuNit);
        } else{
            System.out.println("Categoria no vàlida!");
        }
    }
}
