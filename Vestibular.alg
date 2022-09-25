algoritmo "semnome"
// Função :
// Autor :
// Data : 23/09/2022
// Seção de Declarações 
var
cont, aprovados, reprovado, ap1, ap2, ap3, ap4: inteiro
aluno, melhor_aluno, tu, ma1, ma2, ma3, ma4: caractere
nota, melhor_nota, mn1 , mn2, mn3, mn4: real
inicio
// Seção de Comandos 
escreval("Insira nome e nota dos alunos da turma A")


     cont <- 1
     melhor_nota <- 0
     ap1 <- 0

     para cont de 1 ate 2 faca
     escreval("Aluno", cont)
     escreval("Nome do(a) aluno(a): ")
     leia(aluno)
     escreval("Nota de ", aluno, ": ")
     leia(nota)


              se (nota > mn1) entao
              mn1 <- nota
              ma1 <- aluno

              fimse





        se(nota >= 7)entao

         escreval("Aluno(a) Aprovado!")
         ap1 <- ap1 +1
         fimse

      se(nota <= 6.9)entao

          escreval("Aluno(a) foi reprovado!")

               fimse
               fimpara
               
               se(mn1 > melhor_nota)entao
               melhor_nota <- mn1
               melhor_aluno <- ma1






          escreval("A maior nota da turma A foi do(a): ",ma1, " .Sua nota foi ", mn1)
          escreval("A quantidade de alunos aprovados da turma A foram ", ap1)





      escreval("")
      escreval("Insira nome e nota dos alunos da turma B")
      para cont de 1 ate 2 faca
     escreval("Aluno", cont)
     escreval("Nome do(a) aluno(a): ")
     leia(aluno)
     escreval("Nota de ", aluno, ": ")
     leia(nota)


              se (nota > mn2) entao
              mn2 <- nota
              ma2 <- aluno

              fimse





        se(nota >= 7)entao

         escreval("Aluno(a) Aprovado!")
         ap2 <- ap2 +1
         fimse

      se(nota <= 6.9)entao

          escreval("Aluno(a) foi reprovado!")

               fimse
               fimpara
               
               se(mn2 > melhor_nota)entao
               melhor_nota <- mn2
               melhor_aluno <- ma2
               
               fimse




          escreval("A maior nota da turma B foi do(a): ",ma2, " .Sua nota foi ", mn2)
          escreval("A quantidade de alunos aprovados da turma B foram ", ap2)






     escreval("")
     escreval("Insira nome e nota dos alunos da turma C")
     para cont de 1 ate 2 faca
     escreval("Aluno", cont)
     escreval("Nome do(a) aluno(a): ")
     leia(aluno)
     escreval("Nota de ", aluno, ": ")
     leia(nota)


              se (nota > mn3) entao
              mn3 <- nota
              ma3 <- aluno

              fimse





        se(nota >= 7)entao

         escreval("Aluno(a) Aprovado!")
         ap3 <- ap3 +1
         fimse

      se(nota <= 6.9)entao

          escreval("Aluno(a) foi reprovado!")

               fimse
               fimpara
               
               se(mn3 > melhor_nota)entao
               melhor_nota <- mn3
               melhor_aluno <- ma3
               
               fimse




          escreval("A maior nota da turma C foi do(a): ",ma3, " .Sua nota foi ", mn3)
          escreval("A quantidade de alunos aprovados da turma C foram ", ap3)






     escreval("")
     escreval("Insira nome e nota dos alunos da turma D")
     para cont de 1 ate 2 faca
     escreval("Aluno", cont)
     escreval("Nome do(a) aluno(a): ")
     leia(aluno)
     escreval("Nota de ", aluno, ": ")
     leia(nota)


              se (nota > mn4) entao
              mn4 <- nota
              ma4 <- aluno

              fimse





        se(nota >= 7)entao

         escreval("Aluno(a) Aprovado!")
         ap4 <- ap4 +1
         fimse

      se(nota <= 6.9)entao

          escreval("Aluno(a) foi reprovado!")

               fimse
               fimpara
               
               se(mn4 > melhor_nota)entao
               melhor_nota <- mn4
               melhor_aluno <- ma4
               
               fimSe


           aprovados <- ap1+ap2+ap3+ap4


          escreval("A maior nota da turma D foi do(a): ",ma4, " .Sua nota foi ", mn4)
          escreval("A quantidade de alunos aprovados da turma D foram ", ap4)
          escreval("")
          escreval("De acordo com os dados inseridos, o total de aprovados foram ", aprovados, "!")
          escreval("O melhor aluno entre as turmas A, B, C e D foi ", melhor_aluno, " com a nota ", melhor_nota, "!")
          
          

          fimalgoritmo
