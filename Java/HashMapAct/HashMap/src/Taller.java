import java.util.HashMap;

public class Taller {
    private HashMap<String, Cotxe> miHashMap = new HashMap<String, Cotxe>();


    //Metode afegir cotxe al taller
    public void afegirCotxe(Cotxe cotxe) {
        String clau = cotxe.getMarca() + " " + cotxe.getModel();
        miHashMap.put(clau, cotxe);
    }

    // Mètode per llistar els cotxes del taller
    public void llistarCotxes() {
        for (Cotxe cotxe : miHashMap.values()) {
            System.out.println(cotxe);
        }
    }
}
