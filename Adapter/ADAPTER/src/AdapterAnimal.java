public class AdapterAnimal extends AdaptadorPato {
    private Galinha galinhaa;

    public AdapterAnimal(Galinha galinhaa) {
        this.galinhaa = galinhaa;
    }

    public void pato() {
        galinhaa.galinha();
    }
}
