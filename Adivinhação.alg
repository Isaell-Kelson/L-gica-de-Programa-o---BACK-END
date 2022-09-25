algoritmo "semnome"
// Função :
// Autor :
// Data : 23/09/2022
// Seção de Declarações 
var
resposta, r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10: caractere
   r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21: caractere
   r22, r23, te: caractere
inicio
// Seção de Comandos

escreval("            ====== Pense em um dos meios de transporte a seguir ======")
   escreval("Trator")
   escreval("Moto")
   escreval("Bicicleta")
   escreval("Trem")
   escreval("Carro")
   escreval("Caminhão")
   escreval("Ônibus")
   escreval("Paraquedas")
   escreval("Balão")
   escreval("Avião")
   escreval("Helicóptero")
   escreval("Submarino")
   escreval("Barco")
   escreval("Navio")
   escreval("Lancha")
   escreval("=================================================================")



escreval("O transporte que você pensou é Aéreo, Terrestre ou Aquático?")
leia(te)
escolha te

caso "Terrestre"
             escreval("Cabe apenas uma pessoa? ")
                leia(r0)
                 se (r0 = "sim") entao
               escreval("É pesado? ")
               leia(r1)

       se (r1 = "sim") entao
          escreval("O transporte que você pensou é um TRATOR!")

                 senao
              escreval("Tem pedal? ")
                leia(r2)
            se(r2 = "sim") entao
       escreval("O transporte que você pensou é uma BICICLETA!")

       senao
      escreval("Usa capacete? ")
      leia(r3)
      se(r3 = "sim") entao
      escreval("O transporte que você pensou é uma MOTO!")
      fimse
        fimse
         fimse
        fimse

      se(r0 = "nao") entao
         escreval("Tem passageiro? ")
           leia(r4)
             se(r4 = "sim") entao
               escreval("Usa trilho? ")
                    leia(r5)
                se(r5 = "sim") entao
           escreval("O transporte que você pensou é um TREM!")

            senao
              escreval("Anda na pista? ")
                  leia(r6)
                  se(r6 = "sim") entao
                     escreval("É alto? ")
                      leia(r7)
                    se(r7 = "sim") entao
               escreval("Usa carroceria? ")
              leia(r8)

            se(r8 = "sim") entao
        escreval("O transporte que você pensou é um CAMINHÃO!")

        senao
        escreval("Pode ter cobrador? ")
        leia(r9)
        se(r9 = "sim") entao
        escreval("O transporte que você pensou é um ÔNIBUS!")
        FimSe
              FimSe
            FimSe
           FimSe
            FimSe
             FimSe
              FimSe

        se(r7 = "nao") entao
        escreval("É veículo leve? ")
        leia(r10)
        se(r10 = "sim") entao
        escreval("O transporte que você pensou é um CARRO!")
         FimSe
           FimSe
           fimalgoritmo









caso "Aéreo"
                       escreval("Precisa pular? ")
                   leia(r12)
                se(r12 = "sim") entao
                escreval("O transporte que você pensou é uma ASA DELTA!")

                senao
                escreval("Viaja dentro? ")
                      leia(r13)
                   se(r13 = "sim") entao
                   escreval("É devagar? ")
                 leia(r14)
              se(r14 = "sim") entao
           escreval("O transporte que você pensou é BALÃO!")


                senao
                  escreval("Tem piloto? ")
                  leia(r15)
                    se(r15 = "sim") entao
                  escreval("Possui asas fixas? ")
                  leia(r16)
                    se(r16 = "sim") entao
                escreval("O transporte que você pensou é um AVIÃO!")
              FimSe
                FimSe
              FimSe
            FimSe
            FimSe

                 se(r16 = "nao") entao
                 escreval("Faz voo vertical? ")
                 leia(r17)
                 se(r17 = "sim") entao
                 escreval("O transporte que você pensou é um HELICÓPTERO!")

                   FimSe
                     FimSe
                     fimalgoritmo



caso "Aquático"

              escreval("É coberto d'água? ")
                   leia(r18)
                    se(r18 = "sim") entao
                     escreval("O transporte que você pensou é um SUBMARINO!")
                     senao
                     se(r18 = "nao") entao
                       escreval("Navega na água? ")
                          leia(r19)
                            se(r19 = "sim") entao
                               escreval("Possui vela? ")
                             leia(r20)
                         se(r20 = "sim") entao
                       escreval("O transporte que você escolheu é um BARCO!")

                       fimse
                         fimse
                           fimse
                            fimse



                            se(r20 = "nao") entao
                               escreval("Tem motor? ")
                                  leia(r21)
                                  se(r21 = "sim") entao
                                  escreval("É alto? ")
                                  leia(r22)
                             se(r22 = "sim") entao
                          escreval("O transporte que você pensou é um NAVIO!")
                          fimse
                          fimse
                          fimse



                             se(r22 = "nao") entao
                                  escreval("Pode ser descoberto? ")
                                    leia(r23)
                                 se(r23 = "sim") entao
                              escreval("O transporte que você escolheu é uma LANCHA!")
                         FimSe
                         FimSe
                         fimescolha
                                   fimalgoritmo
