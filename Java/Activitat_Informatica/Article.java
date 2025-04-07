package Activitat_Informatica;

public abstract class Article {
    protected String codi;
    protected String descripcio;
    protected int unitats;
    protected float preuBase;

    public Article(String codi, String descripcio, int unitats, float preuBase) {
        this.codi = codi;
        this.descripcio = descripcio;
        this.unitats = unitats;
        this.preuBase = preuBase;
    }

    public abstract float preu();

    public String getCodi() {
        return codi;
    }

    public String getDescripcio() {
        return descripcio;
    }

    public float getPreuBase() {
        return preuBase;
    }

    public int getUnitats() {
        return unitats;
    }

    //public boolean equals(Object obj){

    //}

    //public int hashCode(){

    //}
}
