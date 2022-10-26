public class App {
    public static void main(String[] args) {
       
        int[] numeros = {7, 8, 6, 2, 42, 200};
        int[] div = {0, 2, 4, 8, 2, 0, 10};

        for(int i=0; i<numeros.length; i++){
            try{
                if(numeros[i] % 2 != 0){
                    throw new Exception("A divisão não está exata, pois é um número ímpar");

                }
                System.out.println(numeros[i] + "/" + div[i] + " = " + (numeros[i]/div[i]));
            }
            catch(ArithmeticException | ArrayIndexOutOfBoundsException a){
                System.out.println("Erro!");
            }
        
            catch(Exception a){
                 System.out.println("Erro!");
                System.out.println(a.getMessage());
            }
         }
    
    }
}