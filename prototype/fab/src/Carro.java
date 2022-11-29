public class Carro extends Veiculo {

    private int roda;

    public Carro(double modelo, double marca, double cor, double numeroRodas) {
        super(modelo, marca, cor, numeroRodas);
        this.roda = 4; 
    }

    public int getRoda() {
        return roda;
    }

    @Override
    public Veiculo copy() {
        System.out.println("Fabricado!" + Carro.class);
        Carro carro = new Carro(this.getModelo(), this.getMarca(), this.getCor(), this.getNumeroRodas());
        return carro;
    }
    
}