public class App {
    public static void main(String[] args) {
        Galinha ga = new Galinha();

        AdapterAnimal a = new AdapterAnimal(ga);
        a.pato();
    }
}
