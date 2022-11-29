public class Carro2 extends Veiculo {
    
    private String tipo;

    public Carro2(double modelo, double marca, double cor, double numeroRodas) {
        super(modelo, marca, cor, numeroRodas);
        this.tipo = "Esportivo";

    }

    public String getTipo() {
        return this.tipo;
    }

    @Override
    public Veiculo copy() {
        System.out.println("Fabricado!" + Carro2.class);
        Carro2 carro2 = new Carro2(this.getModelo(), this.getMarca(), this.getCor(), this.getNumeroRodas());
        return carro2;
    }
}
