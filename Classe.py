class Filme:
   
    __contador = 0
   
   
    def __init__(self, nome=None, ano=None, duracao=None):
        self.__nome = nome
        self.__ano = ano
        self.__duracao = duracao
        __class__.__contador+=1
        print("Informações do filme {}".format(self))

    @staticmethod
    def get_contador():
        return __class__.__contador

    def __str__(self):
        return 'Nome: {}  Ano: {}  Duração: {}'.format(self.__nome, self.__ano, self.__duracao,)

print(Filme.get_contador())
hp = Filme('Harry Potter e a Pedra Filosofal', 2001, 152)
print(hp)



print(Filme.get_contador())
hp2 = Filme('Harry Potter e a Câmara Secreta', 2002, 161)
print(hp2)



print(Filme.get_contador())
hp3 = Filme('Harry Potter e o Prisioneiro de Azakaban', 2004, 142)
print(hp3)   