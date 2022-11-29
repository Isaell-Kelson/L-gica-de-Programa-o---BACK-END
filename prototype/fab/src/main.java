class principal {
    public static void main(String[] args) {
    
        Carro c1 = new Carro(0, 0, 0, 0);
        Carro2 c2 = new Carro2(0, 0, 0, 0);

        fabrica(c1);
        fabrica(c2);
    }



    public static void fabrica (Veiculo v) {
        Veiculo o = v.copy();
        Carro2 c2 = null;
        Carro c1 = null;

        if (o instanceof Carro2) {
            c2 = (Carro2) o;
        }else if (o instanceof Carro) {
            c1 = (Carro) o;
        }
    }
}
