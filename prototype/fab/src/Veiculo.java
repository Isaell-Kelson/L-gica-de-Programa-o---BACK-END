
public abstract class Veiculo {
    private double modelo;
    private double marca;
    private double cor;
    private double numeroRodas;

    public Veiculo(double modelo, double marca, double cor, double numeroRodas) {
        this.modelo = modelo;
        this.marca = marca;
        this.cor = cor;
        this.numeroRodas = numeroRodas;
    }

    

    public double getModelo() {
        return modelo;
    }



    public void setModelo(double modelo) {
        this.modelo = modelo;
    }



    public double getMarca() {
        return marca;
    }



    public void setMarca(double marca) {
        this.marca = marca;
    }



    public double getCor() {
        return cor;
    }



    public void setCor(double cor) {
        this.cor = cor;
    }



    public double getNumeroRodas() {
        return numeroRodas;
    }



    public void setNumeroRodas(double numeroRodas) {
        this.numeroRodas = numeroRodas;
    }



    public String toString() {
        return "Veiculo [modelo=" + this.modelo + ", marca=" + this.marca + ", cor=" + this.cor + ", numeroRodas=" + this.numeroRodas + "]";
    }

    public abstract Veiculo copy();


}
