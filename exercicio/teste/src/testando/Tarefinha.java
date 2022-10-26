package testando;
import java.io.Serializable;
public class Tarefinha implements Serializable {
    private String aluno;
    private String professor;
    private String turno;
    
    public Tarefinha(String aluno, String professor, String turno) {
        this.aluno = aluno;
        this.professor = professor;
        this.turno = turno;
    }
    @Override
    public String toString(){
        return "Tarefinha("+
                "aluno='"+aluno+'\''+
                ", professor='"+professor+'\''+
                ", turno='"+turno+'\''+
                ')';
    }

    public String getAluno() {
        return aluno;
    }

    public void setAluno(String aluno) {
        this.aluno = aluno;
    }

    public String getProfessor() {
        return professor;
    }

    public void setProfessor(String professor) {
        this.professor = professor;
    }

    public String getTurno() {
        return turno;
    }

    public void setTurno(String turno) {
        this.turno = turno;
    }
    

    
}