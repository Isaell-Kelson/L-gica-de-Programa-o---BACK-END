import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import testando.Tarefinha;



public class App {
    public static void main(String[] args) throws Exception {
        salvarTarefinha();
        lertarefinha();
        
    }
    private static void salvarTarefinha (){
        Tarefinha tarefinha = new Tarefinha("Isaell", "Brundre", "B");
        try(ObjectOutputStream obj = new ObjectOutputStream(new FileOutputStream("Tarefinha.txt"))){
            obj.writeObject(tarefinha);
        } catch(IOException e){
            e.printStackTrace();              
        }
    }
    private static void lertarefinha (){
        try(ObjectInputStream objler = new ObjectInputStream(new FileInputStream("Tarefinha.txt"))){
            Tarefinha tarefinha = (Tarefinha) objler.readObject();
            System.out.println(tarefinha);
            objler.close();
        
        } catch(IOException e){
            e.printStackTrace();
        } catch (ClassNotFoundException e){
            e.printStackTrace();
        }
        
    }
}
