import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Creem un taller
        Taller taller = new Taller();

        int opcio;

        do {
            // Mostrem el menú
            System.out.println("Menu:");
            System.out.println("1. Llistar cotxes");
            System.out.println("2. Afegir cotxe");
            System.out.println("3. Sortir");
            System.out.print("Selecciona una opció: ");

            // Llegim l'opció de l'usuari
            opcio = sc.nextInt();
            sc.nextLine();  // Per llegir el salt de línia després de l'enter

            switch (opcio) {
                case 1:
                    taller.llistarCotxes();
                    break;
                    case 2:
                        // Afegim cotxe
                        System.out.print("Introdueix la marca del cotxe: ");
                        String marca = sc.nextLine();

                        System.out.print("Introdueix el model del cotxe: ");
                        String model = sc.nextLine();

                        System.out.print("Introdueix la cilindrada (ex: 2.0): ");
                        String cilindradaStr = sc.nextLine(); // Llegim com a cadena
                        double cilindrada = Double.parseDouble(cilindradaStr.replace(",", "."));

                        System.out.print("Introdueix la potencia del cotxe: ");
                        float potencia = sc.nextFloat();

                        System.out.print("Introdueix la transmissio del cotxe (1 per manual, 2 per Automàtic): ");
                        int transmissioIndex = sc.nextInt();
                        Cotxe.Transmissio transmissio = (transmissioIndex == 1) ? Cotxe.Transmissio.Manual : Cotxe.Transmissio.Automatic;

                        System.out.println("Es hibrid? (True/False): ");
                        boolean hibrid = sc.nextBoolean();
                        sc.nextLine();


                        // Crear i afegir cotxe al taller
                        Cotxe cotxe = new Cotxe(marca, model, cilindrada, potencia, transmissio, hibrid);
                        taller.afegirCotxe(cotxe);
                        System.out.println("El cotxe s'ha afegit correctament");
                        break;
                        case 3:
                            //Sortir
                            System.out.println("Sortint del programa...");
                            break;
                            default:
                                //Opcións incorrectes
                                System.out.println("Opció incorrecta. Prova una opció vàlida!");
                                break;
            }
        } while (opcio != 3); // Continuar fins que l'usuari escolleixi l'opció de sortir
        sc.close();
    }
}
