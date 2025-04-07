package Activitat_Informatica;

import java.util.ArrayList;

public class Botiga {
    private ArrayList<Article> estoc;

    public Botiga() {
        this.estoc = new ArrayList<>();
    }

    public boolean afegirArticle(Article a) {
        if (a == null) {
            return false; // Si el article es null, no el podrem afegir
        }
        estoc.add(a); // Afegeix l'article
        return true; // Retornem true indicant que l'article s'ha afegit
    }

    public boolean esborrarArticle(Article a) {
        if (a == null) {
            return false; // Si es null, no es pot eliminar
        }
        boolean esEliminat = estoc.remove(a); // Elimina l'article i retorna true si el troba o false si no
        return esEliminat; // Retorna true si s'ha eliminat i false si no
    }

    public void llistarEstoc() {
        System.out.println("\nCODI  DESCRIPCIÓ      UNI     CAP/VEL     PREU");
        System.out.println("-----   ----------      ----    --------    ------");
        for (Article a : estoc) {
            System.out.println(a);
        }
    }

    public float valorEstoc() {
        float total = 0;
        int numDiscs = 0;
        int numCpu = 0;
        for (Article a : estoc) {
            total += a.preu() * a.unitats;
            if (a instanceof DiscDur){
                numDiscs += a.unitats;
            }
            else {
                numCpu += a.unitats;
            }
        }
        System.out.println("\nNombre total de discs durs en estoc: "+numDiscs);
        System.out.println("Nombre total de CPUs en estoc: "+numCpu+"\n");

        System.out.println("Valor total de l'estoc: " + total);
        return total;
    }
}
