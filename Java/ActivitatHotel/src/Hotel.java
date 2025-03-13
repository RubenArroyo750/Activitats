import java.util.ArrayList;

public class Hotel {
    private String nom;
    private int numEstrelles;
    private List<Habitacio> habitacions;


    public Hotel(String nom, int numEstrelles, List<Habitacio> habitacions) {
        this.nom = nom;
        this.numEstrelles = numEstrelles;
        this.habitacions = new ArrayList<>();
    }


}
